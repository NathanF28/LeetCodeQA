class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:

        paths = []
        n = len(graph) - 1
        def dfs(node,path):
            if node ==  n:
                paths.append(path[:])
                return
            for neighbor in graph[node]:
                path.append(neighbor)
                dfs(neighbor,path)
                path.pop()
        dfs(0,[0])
        return paths


        