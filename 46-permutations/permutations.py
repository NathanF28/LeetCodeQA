class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = []
        visited = [0] * n
        def backtrack(path,visited):
            if sum(visited) == n:
                res.append(path[:])
                return 
            for i in range(len(nums)):
                if not visited[i]:
                    visited[i] = 1
                    path.append(nums[i])
                    backtrack(path,visited)
                    visited[i] = 0
                    path.pop()
        backtrack([],visited)
        return res