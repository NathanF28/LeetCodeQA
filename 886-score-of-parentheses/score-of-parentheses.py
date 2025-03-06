class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = []
        score = 0
        for char in s:
            if char == ")":
                if stack and stack[-1] == "(":
                    stack.pop()
                    stack.append(1)
                elif stack and stack[-2] == "(":
                    val = stack.pop()
                    stack.pop()
                    stack.append(2*val)
                elif stack and stack[-2] != "(":
                    num = 0
                    while stack and stack[-1] != "(":
                        num+=stack.pop()
                    stack.pop()
                    stack.append(2*num)
            else:
                stack.append(char)
        return sum(stack)
                    
                    
            
        