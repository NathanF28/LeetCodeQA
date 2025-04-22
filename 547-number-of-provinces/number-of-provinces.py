class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        graph = defaultdict(list)
        visited = [False] * len(isConnected)
        count = 0
        for i in range(len(isConnected)):
            for j in range(len(isConnected[0])):
                if i == j:
                    continue
                if isConnected[i][j] == 0:
                    continue
                graph[i].append(j)
        print(graph)
        def dfs(node):
            nonlocal visited
            visited[node] = True
            for neighbor in graph[node]:
                if not visited[neighbor]:
                    dfs(neighbor)
        for i in range(len(isConnected)):
            if not visited[i]:
                dfs(i)
                count+=1
        return count