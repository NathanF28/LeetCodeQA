class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        possible = set()

        def backtrack(index,path):
            nonlocal possible
            if index == len(s): 
                possible.add("".join(path[:]))
                return
            path.append(s[index].lower())
            backtrack(index+1,path)
            path.pop()
            path.append(s[index].upper())
            backtrack(index+1,path)
            path.pop()
            
        backtrack(0,[])
        return list(possible)


