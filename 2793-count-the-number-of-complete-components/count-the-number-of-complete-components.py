class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)
        def isComplete(nodes):
            n = len(nodes)
            start = n - 1
            for node in nodes:
                if len(graph[node]) != start:
                    return False
            return True
        visited = [False] * n
        def dfs(i,path):
            visited[i] = True
            for neighbor in graph[i]:
                if not visited[neighbor]:
                    path.append(neighbor)
                    dfs(neighbor,path)
            return path
        count = 0
        for i in range(n):
            if not visited[i]:
                path = []
                path.append(i)
                x = dfs(i,path)
                if isComplete(x):
                    count+=1
        return count
        