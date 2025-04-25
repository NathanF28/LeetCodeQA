class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        safemap = {}
        n = len(graph)
        def dfs(i):
            if i in safemap:
                return safemap[i]
            safemap[i] = False
            for neighbor in graph[i]:
                if not dfs(neighbor):
                    return False
            safemap[i] = True
            return True
        res = []
        for i in range(n):
            if dfs(i):
                res.append(i)
        return res 