from sortedcontainers import SortedList
class Solution:
    def createSortedArray(self, instructions: List[int]) -> int:
        arr = SortedList()
        arr.add(instructions[0])
        count = 0
        for num in instructions[1:]:
            bl = arr.bisect_left(num)
            br = arr.bisect_right(num)
            count+= min(len(arr)-br,bl)
            count %=  (10**9 + 7)
            arr.add(num)
        return count  

        