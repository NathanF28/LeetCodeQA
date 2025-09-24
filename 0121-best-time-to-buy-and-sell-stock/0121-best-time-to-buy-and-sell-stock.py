class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        best = 0
        _min = prices[0]
        for i in range(1,len(prices)):
            best = max(best, prices[i] - _min)
            _min = min(_min, prices[i])
        return best


        