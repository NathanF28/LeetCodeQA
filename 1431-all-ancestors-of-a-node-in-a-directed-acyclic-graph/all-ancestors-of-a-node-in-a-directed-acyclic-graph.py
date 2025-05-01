class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        graph = defaultdict(list)
        indeg = defaultdict(int)
        for u,v in edges:
            graph[u].append(v)
            indeg[v]+=1
        answer = []
        ancestor = defaultdict(set)
        q = deque()
        for i in range(n):
            if indeg[i] == 0:
                q.append(i)
        while q:
            node = q.popleft()
            for neighbor in graph[node]:
                ancestor[neighbor].add(node)
                ancestor[neighbor].update(ancestor[node])
                indeg[neighbor]-=1
                if indeg[neighbor] == 0:
                    q.append(neighbor)
            
        for i in range(n):
            answer.append(list(sorted(ancestor[i]))) 
        return answer