class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        # storing positions of ones first
        positions = []
        for i in range(rows):
            for j in range(cols):
                if grid[i][j]:
                    positions.append((i,j))
        max_squares = 0
        visited = set()

        directions = [(0,1),(1,0),(0,-1),(-1,0)]
        def inbound(row,col):
            return 0 <= row < rows and 0 <= col < cols

        def dfs(row,col):
            square = 1
            for dr,dc in directions:
                nr = dr + row
                nc = dc + col
                if inbound(nr,nc) and (nr,nc) not in visited and grid[nr][nc] != 0:
                    visited.add((nr,nc))
                    square += dfs(nr,nc)
            return square


        for x,y in positions:
            if (x,y) not in visited:
                visited.add((x,y))
                val = dfs(x,y)
                max_squares = max(max_squares, val)

        return max_squares


        
        