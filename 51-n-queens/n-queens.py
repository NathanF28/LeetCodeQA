class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        possible = []
        check = set()
        left = set()
        right = set()
        def backtrack(row,path):
            if len(path) == n:
                possible.append(path[:])
                return
            for i in range(n):
                if i not in check and (row - i) not in left and (row + i) not in right:
                    string = ("." * (i)) + "Q" + ("." * (n-i-1))
                    path.append(string)
                    left.add(row-i)
                    right.add(row+i)
                    check.add(i)
                    backtrack(row+1,path)
                    check.remove(i)
                    left.remove(row-i)
                    right.remove(row+i)
                    path.pop()
        backtrack(0,[])
        return possible 
                

        