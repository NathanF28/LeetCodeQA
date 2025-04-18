"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        graph = defaultdict(list)
        for employee in employees:
            graph[employee.id].append(employee.importance)
            graph[employee.id].extend(employee.subordinates)
        def dfs(node):
            if len(graph[node]) == 1:
                return graph[node][0] 
            imp = graph[node][0]
            for sub in graph[node][1:]:
                imp += dfs(sub) 
            return imp
        x = dfs(id)
        return x


        