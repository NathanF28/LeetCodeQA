class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        directions = {
        1: [(0, -1), (0, 1)], 
        2: [(1, 0), (-1, 0)], 
        3: [(0, -1), (1, 0)],
        4: [(0, 1), (1, 0)],  
        5: [(0, -1), (-1, 0)], 
        6: [(0, 1), (-1, 0)]   
        }
        valid = {
        1: [(1, 4, 6), (1, 3, 5)],  
        2: [(2, 5, 6), (2, 3, 4)],  
        3: [(1, 4, 6), (2, 5, 6)], 
        4: [(1, 3, 5), (2, 5, 6)], 
        5: [(1, 4, 6), (2, 3, 4)], 
        6: [(1, 3, 5), (2, 3, 4)]  
    }
        def inbound(row,col):
            return 0 <= row < len(grid) and 0 <= col < len(grid[0])
        visited = [[False for _ in range(len(grid[0]))] for __ in range(len(grid))]
        possible = False
        def dfs(row,col):
            nonlocal possible
            visited[row][col] = True
            if row == len(grid) -1 and col == len(grid[0])-1:
                possible = True
            for index,direction in enumerate(directions[grid[row][col]]):
                nr = row + direction[0]
                nc = col + direction[1]
                if inbound(nr,nc) and not visited[nr][nc] and grid[nr][nc] in valid[grid[row][col]][index]:
                    dfs(nr,nc)
        dfs(0,0)
        return possible 
