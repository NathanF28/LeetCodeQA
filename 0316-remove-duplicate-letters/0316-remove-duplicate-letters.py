class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        last = {}
        for index, char in enumerate(s):
            last[char] = index
        stack = []          
        seen = set()

        for i in range(len(s)):
            if s[i] in seen:
                continue
            while stack and s[i] < stack[-1] and i < last[stack[-1]]:
                seen.remove(stack.pop())

            stack.append(s[i])
            seen.add(s[i])    
        return "".join(stack)