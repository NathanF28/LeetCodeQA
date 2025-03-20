class Solution:
    def splitString(self, s: str) -> bool:
        splits = []
        def backtrack(string,check):
            if len(check) >= 2:
                if check[-1] != check[-2] - 1:
                    return
            if string == "":
                if len(check) > 1:
                    splits.append([check])
                return

            for i in range(len(string)):
                to_left = int(string[:i+1])
                check.append(to_left)
                to_right = string[i+1:]
                backtrack(to_right,check)
                check.pop()
        backtrack(s,[])
        return len(splits) != 0
        