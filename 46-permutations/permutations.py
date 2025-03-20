class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)
        visited = [0] * n
        def backtrack(path):
            if len(path) == n:
                res.append(path[:])
                return
            for i in range(n):
                if not visited[i]:
                    visited[i] = 1
                    path.append(nums[i])
                    backtrack(path)
                    visited[i] = 0
                    path.pop()
        backtrack([])
        return res
        