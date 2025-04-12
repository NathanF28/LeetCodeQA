class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = defaultdict(list)
        visited = [0] * n 
        for liste in edges:
            graph[liste[0]].append(liste[1])
            graph[liste[1]].append(liste[0])
        found = False
        def dfs(node):
            nonlocal visited
            nonlocal found
            if node == destination:
                found = True
                return
            visited[node] = 1
            for neighbor in graph[node]:
                if not visited[neighbor]:
                    dfs(neighbor)
        dfs(source) 
        return found
