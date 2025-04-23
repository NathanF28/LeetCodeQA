class Solution:
    def isBipartite(self, g: List[List[int]]) -> bool:
        colormap = {}
        graph = defaultdict(list)
        for i in range(len(g)):
            graph[i].extend(g[i])
        visited = [False] * len(graph)
        false = True
        def dfs(node,color):
            nonlocal visited
            nonlocal graph
            nonlocal false
            nonlocal colormap
            if visited[node]:
                if color != colormap[node]:
                    false = False
                return
            colormap[node] = color
            visited[node] = True
            for neighbor in graph[node]:
                dfs(neighbor,1-color)

        for i in range(len(graph)):
            if not visited[i]:
                dfs(i,0)
        return false 


        




        