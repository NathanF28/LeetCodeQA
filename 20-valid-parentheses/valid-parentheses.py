class Solution:
    def isValid(self, s: str) -> bool:
        map = {")": "(", "}" : "{" , "]": "["}
        stack = []
        for char in s:
            if char in map:
                if stack and stack[-1] != map[char]:
                    return False
                elif stack:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)
        return not stack
                    
        