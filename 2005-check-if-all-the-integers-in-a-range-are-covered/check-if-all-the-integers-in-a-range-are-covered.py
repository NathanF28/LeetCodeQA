class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        
        for number in range(left, right + 1):
            covered = False

            for start, end in ranges:
                if number >= start and number <= end:
                    covered = True
                
            if covered == False:
                return False
        return True
