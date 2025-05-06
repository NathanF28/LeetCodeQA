class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        directions = [(0,1),(1,0),(-1,0),(0,-1)]
        smallrow,smallcol = len(grid),len(grid[0])
        bigrow,bigcol= 3 * smallrow, 3 * smallcol
        expanded = [[0 for _ in range(bigcol)] for _ in range(bigrow)]
        visited = [[False for _ in range(bigcol)] for _ in range(bigrow)]
        for i in range(smallrow):
            for j in range(smallcol):
                r, c = 3 * i, 3 * j
                if grid[i][j] == "/":
                    expanded[r][c + 2] = 1
                    expanded[r + 1][c + 1] = 1
                    expanded[r + 2][c] = 1
                elif grid[i][j] == "\\":
                    expanded[r][c] = 1
                    expanded[r + 1][c + 1] = 1
                    expanded[r + 2][c + 2] = 1
        count = 0
        def inbound(row,col):
            return 0 <= row < bigrow and 0 <= col < bigcol
        def dfs(row,col):
            visited[row][col] = True
            for dr,dc in directions:
                nr = dr + row
                nc = dc + col
                if inbound(nr,nc) and not visited[nr][nc] and not expanded[nr][nc]:
                    dfs(nr,nc)
        for i in range(bigrow):
            for j in range(bigcol):
                if not visited[i][j] and not expanded[i][j]:
                    dfs(i,j)
                    count+=1
        return count

        
                    