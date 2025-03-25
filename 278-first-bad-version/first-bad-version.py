# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        l = 1
        r = n
        while l <= r:
            mid = (l+r) //2
            if isBadVersion(mid):
                if mid != 1 and not isBadVersion(mid-1):
                    return mid
                if mid == 1 and isBadVersion(mid):
                    return 1
                else:
                    r = mid - 1

            else:
                l = mid+1
