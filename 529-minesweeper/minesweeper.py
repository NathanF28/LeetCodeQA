class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        directions = [(1,0),(1,1),(0,1),(-1,1),(0,-1),(-1,-1),(-1,0),(1,-1)]
        visited = [[False for _ in range(len(board[0]))] for __ in range(len(board))]
        def inbound(row,col):
            return 0 <= row < len(board) and 0 <= col < len(board[0])
        def isNearby(row,col):
            count = 0
            for dr,dc in directions:
                if inbound(row+dr,col+dc) and board[row+dr][col+dc] == "M":
                    count+=1
            return count
        def neighbors(row,col):
            nonlocal visited
            path = []
            for dr,dc in directions:
                if inbound(row+dr,col+dc) and not visited[row+dr][col+dc]:
                    visited[row][col] = True
                    path.append([row+dr,col+dc])
            return path 
        def mark(path):
            for i,j in path:
                visited[i][j] = True
                if board[i][j] == "M":
                    board[i][j] = "X"
                elif isNearby(i,j):
                    board[i][j] = str(isNearby(i,j))
                else:
                    board[i][j] = "B"
                    mark((neighbors(i,j)))

        i,j = click
        mark([[i,j]])           
        return board 
        