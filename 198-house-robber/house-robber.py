class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [0] * len(nums)
        dp[0] = nums[0]

        for i in range(1,len(nums)):
            val = dp[i-2] if i - 2 >=0 else 0
            cand1 = val + nums[i]
            cand2 = dp[i-1]
            dp[i] = max(cand1,cand2)
        return dp[-1]