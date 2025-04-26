class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        directions = [(0,1), (1,0), (-1,0), (0,-1)]
        rows = len(mat)
        cols = len(mat[0])

        def inbound(row, col):
            return 0 <= row < rows and 0 <= col < cols
        q = deque()
        for i in range(rows):
            for j in range(cols):
                if mat[i][j] == 0:
                    q.append([i,j])
                else:
                    mat[i][j] = float('inf')
        while q:
            row,col = q.popleft()
            for dr,dc in directions:
                nr = row+dr
                nc = col+dc
                if inbound(nr,nc) and mat[nr][nc] > mat[row][col] + 1:
                    mat[nr][nc] = mat[row][col]+1
                    q.append([nr,nc])
        return mat