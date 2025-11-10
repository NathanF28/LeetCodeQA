class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        #dp[i] is cost from ith day to the last day
        last = max(days)
        dp = [0] * (last + 31)
        trav = set(days)
        for i in range(last,-1,-1):
            if i not in trav:
                dp[i] = dp[i+1]
            else:
                dp[i] = min(
                    costs[0] + dp[i+1],
                    costs[1] + dp[i+7],
                    costs[2] + dp[i+30]
                )
        return dp[0]