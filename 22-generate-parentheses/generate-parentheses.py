class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        possible = []
        def backtrack(path,val):
            if val < 0 or val > n:
                return
            if len(path) == 2*n:
                if val == 0:
                    brack = "".join(path[:])
                    possible.append(brack)
                return
            for take in '()':
                if take == "(":
                    val+=1
                else:
                    val-=1
                path.append(take)
                backtrack(path,val)
                path.pop()
                if take == "(":
                    val-=1
                else:
                    val+=1
        backtrack([],0)
        return possible