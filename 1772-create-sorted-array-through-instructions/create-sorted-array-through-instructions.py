from typing import List
from sortedcontainers import SortedList

class Solution:
    def createSortedArray(self, instructions: List[int]) -> int:
        arr = SortedList()
        count = 0
        MOD = 10**9 + 7
        
        for num in instructions:
            bl = arr.bisect_left(num)
            br = len(arr) - arr.bisect_right(num)
            count += min(bl, br)
            count %= MOD
            arr.add(num)
        
        return count
