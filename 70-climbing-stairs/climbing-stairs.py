class Solution:
    def climbStairs(self, n: int) -> int:
        dp = {}
        dp[1] = 1
        dp[2] = 2
        def climb(num):
            if num not in dp:
                dp[num] = climb(num-1) + climb(num-2)
            return dp[num]
        return climb(n)