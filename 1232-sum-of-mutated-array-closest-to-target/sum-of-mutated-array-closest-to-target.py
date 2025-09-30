from bisect import bisect_left
from typing import List

class Solution:
    def findBestValue(self, arr: List[int], target: int) -> int:
        arr.sort()
        val = float('inf')
        od = float('inf')
        l = 0
        r = arr[-1]

        while l <= r:
            i = (l + r) // 2
            pos = bisect_left(arr, i)
            sume = sum(arr[:pos]) + (len(arr) - pos) * i
            diff = abs(target - sume)
            
            if diff < od or (diff == od and i < val):
                od = diff
                val = i

            if sume < target:
                l = i + 1
            else:
                r = i - 1

        return val
