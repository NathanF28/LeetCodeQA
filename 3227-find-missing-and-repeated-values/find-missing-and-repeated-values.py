class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        row = len(grid)
        col = len(grid[0])
        map = {}
        liste = []
        for i in range(row):
            for j in range(col):
                liste.append(grid[i][j])
        map = Counter(liste)
        for key,value in map.items():
            if value == 2:
                a = key
        for i in range(1, (row*col)+1):
            if i not in map:
                b = i
        return [a,b]