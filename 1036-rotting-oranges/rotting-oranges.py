class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        directions = [(0,1),(1,0),(0,-1),(-1,0)]
        def inbound(row,col):
            return 0 <= row < len(grid) and 0 <= col < len(grid[0])
        rottens = []
        count = 0
        visited = [ [False for _ in range(len(grid[0]))] for _ in range(len(grid)) ]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    rottens.append([i,j])
                    visited[i][j] = True
                if grid[i][j] == 1:
                    count+=1
        res = -1
        def bfs(oranges,time):
            nonlocal visited
            nonlocal count
            nonlocal res
            next = [] 
            print(oranges,count,time)
            if count == 0:
                res = time
                return
            for liste in oranges:
                for direction in directions:
                    new_row = liste[0] + direction[0]
                    new_col = liste[1] + direction[1]
                    if inbound(new_row,new_col) and not visited[new_row][new_col] and grid[new_row][new_col]:
                        visited[new_row][new_col] = True
                        if grid[new_row][new_col] == 1:
                            count-=1
                        next.append([new_row,new_col])
            if len(next) != 0:
                bfs(next,time+1)
        bfs(rottens,0)
        return res

