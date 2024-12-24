class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        last = {}
        for i,num in enumerate(s):
            last[num] = i
        stack  = []
        seen = set()
        for i in range(len(s)):
            if s[i] in seen:
                continue
            while stack and stack[-1] > s[i] and last[stack[-1]] > i:
                seen.remove(stack.pop())
            stack.append(s[i])
            seen.add(s[i])
        return "".join(stack)                
        