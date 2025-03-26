class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        liste  = []
        for pair in grid:
            liste.extend(pair)
        liste.sort()
        median = liste[len(liste)//2]
        count = 0
        for num in liste:
            if abs(num - median) / x > abs(num-median) // x:
                return -1
            else:
                count+= abs(num - median) // x
        return count