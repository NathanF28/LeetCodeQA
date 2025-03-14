class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        sume = sum(candies)
        if sume < k:
            return 0
        count = 0
        val = sume // k
        l,r = 1, val
        while l<=r:
            mid = (l+r)//2
            res = 0
            for c in candies:
                if c >= mid:
                    res+=c//mid
            if res >= k:
                count = mid
                l = mid+1
            else:
                r = mid-1
        return count 
