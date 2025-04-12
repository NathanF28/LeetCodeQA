class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        graph = defaultdict(list)
        for liste in dislikes:
            graph[liste[0]].append(liste[1])
            graph[liste[1]].append(liste[0])
        colormap = {}
        def dfs(node, color):
            if node in colormap:
                return colormap[node] == color
            colormap[node] = color

            for neighbor in graph[node]:
                if not dfs(neighbor,1-color):
                    return False
            return True


        for i in range (1, n+1):
            if i not in colormap:
                if not dfs (i,0):
                    return False
        return True
