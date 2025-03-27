class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        l = 1
        r = max(candies)
        if sum(candies) < k:
            return 0
        def validate(n):
            count = 0
            for candy in candies:
                if candy >= n:
                    count+= candy // n
            return count >= k
        while l <= r:
            mid = (l+r)//2
            if validate(mid):
                l = mid + 1
            else:
                r = mid-1
        return r
            

        