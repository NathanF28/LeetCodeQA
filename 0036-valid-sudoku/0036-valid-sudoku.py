class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        mat = [[] for i in range(9)]
        map = defaultdict(list)
        for i in range(len(board)):
            row_checker = set()
            for j in range(len(board[i])):
                value = board[i][j]
                if value != ".":
                    a = i //3
                    b = j //3
                    if value in map[(a,b)]:
                        return False
                    else:
                        map[(a,b)].append(value)
                    if board[i][j] not in row_checker:
                        row_checker.add(value)
                    else:
                        return False
                    if board[i][j] not in mat[j]:
                        mat[j].append(value)
                    else:
                        print("its the list")
                        print(mat[j])
                        print(value)
                        return False
        return True



        

        