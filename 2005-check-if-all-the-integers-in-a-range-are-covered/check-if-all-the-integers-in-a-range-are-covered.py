class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        array = [0] * 52
        for start, end in ranges:
            array[start] += 1
            array[end+1] -=1 

        for i in range(1, len(array)):
            array[i] += array[i-1] 

        for number in range(left,right+1):
            if array[number] == 0:
                return False
        return True