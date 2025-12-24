class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)

        for u,v,w in times:
            graph[u].append([v,w])
        

        dist = [float('inf')] * (n+1)

        dist[k] = 0
        heap = [(0,k)]

        while heap:
            d, node = heappop(heap)

            if d > dist[node]:
                continue
            
            for nei,w in graph[node]:
                new_dist = w + d
                if new_dist < dist[nei]:
                    dist[nei] = new_dist
                    heappush(heap,[new_dist,nei])
        
        ans = max(dist[1:])
        return ans if ans != float('inf') else -1
        