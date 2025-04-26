class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        directions = [(0,1),(1,0),(-1,0),(0,-1)]
        rows = len(grid)
        cols = len(grid[0]) 
        q = deque()
        count = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 2:
                    q.append([i,j])
                elif grid[i][j] == 1:
                    count+=1
        minutes = 0
        if count == 0:
            return 0
        def inbound(row,col):
            return 0 <= row < rows and 0 <= col < cols
        while q: 
            print(q)
            minutes+=1
            for _ in range(len(q)):
                row,col = q.popleft()
                for dr,dc in directions:
                    nr = row+dr
                    nc = col+dc
                    if inbound(nr,nc) and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        count-=1
                        q.append([nr,nc])
            if count == 0:
                break
        return minutes if count == 0 else -1

