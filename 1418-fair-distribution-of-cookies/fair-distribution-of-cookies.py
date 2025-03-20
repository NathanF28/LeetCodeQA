class Solution:
    def distributeCookies(self, nums: List[int], k: int) -> int:
        child = [0] * k
        unfair = float('inf')
        def backtrack(start):
            nonlocal unfair
            if start == len(nums):
                unfair = min(unfair,max(child))
                return
            if max(child) >= unfair:
                return
            for i in range(k):
                child[i] +=nums[start]
                backtrack(start+1)
                child[i]-=nums[start]
        backtrack(0)
        return unfair
