class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        directions = [(0,1), (1,0), (-1,0), (0,-1)]
        rows = len(board)
        cols = len(board[0])

        def inbound(row, col):
            return 0 <= row < rows and 0 <= col < cols

        def edgebound(row, col):
            return row == 0 or row == rows - 1 or col == 0 or col == cols - 1

        safe = set()
        unsafe = set()
        visited = [[False for _ in range(cols)] for _ in range(rows)]

        def dfs(row, col, path):
            nonlocal found
            if edgebound(row, col):
                found = False
            path.append((row, col))
            visited[row][col] = True
            for dr, dc in directions:
                nr, nc = row + dr, col + dc
                if inbound(nr, nc) and not visited[nr][nc] and board[nr][nc] == "O":
                    dfs(nr, nc, path)

        for i in range(rows):
            for j in range(cols):
                if (i, j) in safe:
                    continue
                elif (i, j) in unsafe:
                    board[i][j] = "X"
                    continue
                elif board[i][j] == "X":
                    continue
                path = []
                found = True  
                dfs(i, j, path)
                if found:
                    for r, c in path:
                        unsafe.add((r, c))
                        board[r][c] = "X"
                else:
                    for r, c in path:
                        safe.add((r, c))
        return
