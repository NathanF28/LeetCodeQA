class Solution:
    def dailyTemperatures(self, temp: List[int]) -> List[int]:
        stack = [0]
        res = [0] * len(temp)
        for i in range(1,len(temp)):
            while stack and temp[i] > temp[stack[-1]]:
                val = stack[-1]
                res[stack.pop()] = i - val
            stack.append(i)
        return res

                