class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        n = len(arr)
        next = [n] * n
        stack = []
        for i in range(len(arr)):
            while stack and arr[i] <= arr[stack[-1]]:
                next[stack[-1]] = i
                stack.pop()
            stack.append(i)
        stack = []
        prev = [-1] * n
        for i in range(n-1,-1,-1):
            while stack and arr[i] < arr[stack[-1]]:
                prev[stack[-1]] = i
                stack.pop()
            stack.append(i)
        score = 0
        for i in range(n):
            score+= abs(i - next[i]) * arr[i] * abs(i-prev[i])
        return score % (10**9 + 7)
