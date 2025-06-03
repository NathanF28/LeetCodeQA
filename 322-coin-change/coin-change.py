class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins = sorted(coins)[::-1]
        dp = {}
        def best_split(amount):
            if amount < 0:
                return float('inf')
            if amount == 0:
                return 0
            if amount in dp:
                return dp[amount]
            div = 0
            mine = float('inf')
            for split in coins:
                rem = amount - split
                div = 1 + best_split(rem)
                mine = min(mine,div)
            dp[amount] = mine
            return mine
        x = best_split(amount)
        return x if x != float('inf') else -1
