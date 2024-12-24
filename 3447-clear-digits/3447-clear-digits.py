class Solution:
    def clearDigits(self, s: str) -> str:
        stack = []
        for val in s:
            if stack and val.isdigit():
                stack.pop()
            else:
                stack.append(val)
        stack = "".join(stack)        
        return stack            
        