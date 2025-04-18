class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        directions = [(0,1),(1,0),(0,-1),(-1,0)]
        visited = [[False for _ in range(len(grid[0]))] for _ in range(len(grid))]
        def inbound(row,col):
            return 0 <= row < len(grid) and 0 <= col < len(grid[0])
        longest = 0
        def dfs(row,col):
            nonlocal visited
            nonlocal longest
            if not inbound(row,col) or visited[row][col] or grid[row][col] == 0:
                return 0
            visited[row][col] = True
            val = 1
            for direction in directions:
                new_row = row + direction[0]
                new_col= col + direction[1]
                val += dfs(new_row,new_col)
            longest = max(val,longest)
            return val
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                dfs(i,j)
        return longest