class Solution:
    def isValid(self, s: str) -> bool:
        map = {')': '(', '}': '{', ']': '['}
        stack = []
        for bracket in s:
            if bracket not in map:
                stack.append(bracket)
            else:
                if stack and stack[-1] == map[bracket]:
                    stack.pop()
                else:
                    return False
        return not stack