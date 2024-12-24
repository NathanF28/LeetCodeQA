class Solution:
    def isValid(self, s: str) -> bool:
        map = {')': '(', '}': '{', ']': '['}
        stack = []
        for brack in s:
            if brack not in map:
                stack.append(brack)
            else:
                if stack and stack[-1] == map[brack]:
                    stack.pop()    
                else:
                    return False
        return not stack                
        