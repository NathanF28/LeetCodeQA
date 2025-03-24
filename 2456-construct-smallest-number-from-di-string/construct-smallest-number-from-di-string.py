class Solution:
    def smallestNumber(self, pattern: str) -> str:
        nums = set()
        possible = []
        def backtrack(path,flag,index):
            if flag == "S":
                possible.append(path[:])
                return
            for i in range(1,10):
                if flag == "I":
                    if i > int(path[-1]) and i not in nums:
                        path.append(str(i))
                        nums.add(i)
                        if index == len(pattern) - 1:
                            check = "S"
                        else:
                            check = pattern[index+1]
                        backtrack(path,check,index+1)  
                        path.pop()
                        nums.remove(i)
                    else:
                        continue
                else:
                    if i < int(path[-1]) and i not in nums:
                        path.append(str(i))
                        nums.add(i)
                        if index == len(pattern) - 1:
                            check = "S"
                        else:
                            check = pattern[index+1]
                        backtrack(path,check,index+1)  
                        path.pop()
                        nums.remove(i)
        for i in range(1,10):
            nums.add(i)
            backtrack([str(i)],pattern[0],0)
            nums.remove(i)
        return "".join(sorted(possible)[0])