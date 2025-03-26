class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        def time(num):
            count = 0
            for pile in piles:
                count+= ceil(pile / num)
            return count <= h
        while l < r:
            mid = (l+r) // 2
            if time(mid):
                r = mid
            else:
                l = mid + 1
        return l


        