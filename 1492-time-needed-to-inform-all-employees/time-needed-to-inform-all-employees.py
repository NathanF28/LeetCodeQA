class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        graph = defaultdict(list)
        for i in range(len(manager)):
            if manager[i] == -1:
                continue
            graph[manager[i]].append(i)
        def dfs(node):
            if len(graph[node]) == 0:
                return 0
            _max = 0
            for neighbor in graph[node]:
                _max = max(_max,dfs(neighbor))
            return informTime[node] + _max
        x = dfs(headID)
        return x
        