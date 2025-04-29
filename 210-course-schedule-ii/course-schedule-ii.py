class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        indeg = defaultdict(int)
        for course,prereq in prerequisites:
            graph[prereq].append(course)
            indeg[course]+=1

        q = deque()
        final = []
        for i in range(numCourses):
            if not indeg[i]:
                q.append(i)
        while q:
            prereq =q.popleft()
            final.append(prereq)
            for course in graph[prereq]:
                indeg[course]-=1
                if not indeg[course]:
                    q.append(course)
        return final if len(final) == numCourses else []