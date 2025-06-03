class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0] * (amount + 1)
        dp[0] = 1  # 1 way to make amount 0: pick nothing
    
        for coin in coins:
            for x in range(coin, amount + 1):
                dp[x] += dp[x - coin]
    
        return dp[amount]
    