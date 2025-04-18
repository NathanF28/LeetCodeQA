class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        graph = [[] for i in range(n)]
        indegree = defaultdict(int)
        for edge in edges:
            indegree[edge[1]]+=1
        if n - len(indegree) > 1:
            return -1
        for i in range(n):
            if indegree[i] == 0:
                return i