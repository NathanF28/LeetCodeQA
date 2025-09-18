class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for char in s:
            if char == "]":
                alphabets = ""
                while stack and stack[-1] != "[":
                    alphabets = stack.pop() + alphabets
                stack.pop()
                digits = ""
                while stack and stack[-1].isdigit():
                    digits = stack.pop() + digits
                substring = int(digits) * alphabets
                stack.append(substring)
            else:
                stack.append(char)
        return "".join(stack)