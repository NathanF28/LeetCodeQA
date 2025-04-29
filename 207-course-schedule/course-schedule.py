class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        visited = set()
        safe = set()
        graph = defaultdict(list)
        for u,v in prerequisites:
            graph[u].append(v)
        def dfs(i):
            if i in safe:
                return True
            nonlocal visited
            val = True
            for neighbor in graph[i]:
                if neighbor in visited:
                    val = val and False
                else:
                    visited.add(i)
                    val = val and dfs(neighbor)
                    visited.remove(i)
            if val:
                safe.add(i)
            return val

        for i in range(numCourses):
            if i not in visited:
                visited = set()
                visited.add(i)
                if not dfs(i):
                    return False
        return True
        
        