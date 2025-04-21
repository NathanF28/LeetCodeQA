class Solution:
    def numberOfArrays(self, diff: List[int], lower: int, upper: int) -> int:
        for i in range(1,len(diff)):
            diff[i]+= diff[i-1]
        _max = max(diff)
        _min = min(diff)
        left = max(lower,lower - _min)
        right_min = _max + left
        count = 0
        while left <= upper and right_min <= upper:
            count+=1
            left+=1
            right_min+=1
        return count