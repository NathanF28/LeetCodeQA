class Solution:
    def splitString(self, s: str) -> bool:
        splits = []
        def backtrack(string,path):
            if len(path) >= 2:
                if path[-1] != path[-2] - 1:
                    return 
            if string == "":
                if len(path) > 1:
                    splits.append(path[:])
                    print(path)
                return
            for i in range(len(string)):
                to_left = int(string[:i+1])
                path.append(to_left)
                to_right = string[i+1:]
                backtrack(to_right,path)
                path.pop()
        backtrack(s,[])
        return len(splits) != 0
