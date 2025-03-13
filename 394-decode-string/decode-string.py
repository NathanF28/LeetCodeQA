class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for i in range(len(s)):
            if s[i] == "]":
                string = ""
                while stack and stack[-1] != "[":
                    string = stack.pop() + string
                stack.pop()
                k = ""
                while stack and stack[-1].isdigit():
                    k = stack.pop() + k 
                stack.append(int(k) * string)
            else:
                stack.append(s[i])
        return "".join(stack)


        