class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)


        def time(num):
            count = 0
            for pile in piles:
                count+= ceil(pile / num)
            return count <= h
        while l <= r:
            mid = (l+r) // 2
            if time(mid):
                if mid == 1:
                    return mid
                if not time(mid-1):
                    return mid
                else:
                    r = mid - 1
            else:
                l = mid + 1


        