class Solution:
    def rob(self, nums: List[int]) -> int:
        


        dp = [0] * len(nums)
        dp[0] = nums[0]

        for i in range(1,len(nums)):
            cand1 = dp[i-1]
            cand2 = nums[i] + dp[i-2] if i > 1 else nums[i]
            dp[i] = max(cand1,cand2)
        return dp[-1]