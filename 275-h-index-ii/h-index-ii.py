class Solution:
    def hIndex(self, citations: List[int]) -> int:
        l = 0
        r = max(citations)
        while l <=r:
            mid = (l+r) //2
            bl = bisect_left(citations,mid)
            if len(citations) - bl >= mid:
                l = mid + 1
            else:
                r = mid - 1
        return r
