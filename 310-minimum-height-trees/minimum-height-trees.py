class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        indeg = defaultdict(int)
        if n == 1:
            return [0]
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)
            indeg[u]+=1
            indeg[v]+=1
        q = deque()
        for leaf in range(n):
            if indeg[leaf] == 1:
                q.append(leaf)
        size = n
        while size > 2:
            size-=len(q)
            for i in range(len(q)):
                node = q.popleft()
                print(node)
                for neighbor in graph[node]:
                    indeg[neighbor]-=1
                    if indeg[neighbor] == 1:
                        q.append(neighbor)
            
        return list(q)
            
        
        