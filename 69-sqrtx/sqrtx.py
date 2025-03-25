class Solution:
    def mySqrt(self, x: int) -> int:
        l = 0
        r = x // 2
        if x == 0:
            return 0
        if x == 1:
            return 1
        while l<=r:
            mid = (l+r) // 2
            next = mid + 1
            if mid * mid < x:
                if next * next > x:
                    return mid
                l = mid+1
            elif mid * mid > x:
                r = mid-1
            else:
                return mid
        

        