class Solution:
    def isBipartite(self, g: List[List[int]]) -> bool:
        colormap = {}
        graph = defaultdict(list)
        for i in range(len(g)):
            graph[i].extend(g[i])
        visited = [False] * len(graph)
        false = True
        print(graph)
        def dfs(node,color):
            nonlocal visited
            nonlocal graph
            nonlocal false
            nonlocal colormap

            if visited[node]:
                return color == colormap[node]
            colormap[node] = color
            visited[node] = True
            for neighbor in graph[node]:
                if not dfs(neighbor,1-color):
                    return False
            return True 
            

        for i in range(len(graph)):
            if not visited[i]:
                if not dfs(i,0):
                    return False
        return True

        




        