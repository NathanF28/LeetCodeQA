class Solution:
    def minimumArea(self, grid: List[List[int]]) -> int:
        rw = len(grid)
        cl = len(grid[0])
        tl, tr,bl,br = rw,0,0,rw
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]:
                    tl = min(i,tl)
                    tr = max(j,tr)
                    br = min(j,br)
                    bl = max(i,bl)
        l = tr - br + 1
        r = bl - tl + 1
        return l*r





        