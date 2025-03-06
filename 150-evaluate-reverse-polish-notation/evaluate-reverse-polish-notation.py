class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        op = ["*", "+", "-", "/"]
        for char in tokens:
            if char not in op:
                stack.append(char)
            else:
                a = int(stack.pop())
                b = int(stack.pop())
                if char == "+":
                    stack.append(a + b)
                elif char == "-":
                    stack.append(b - a)
                elif char == "*":
                    stack.append(a * b)
                elif char == "/":
                    stack.append(b // a) if b * a > 0 else stack.append(ceil(b / a))
        return int(stack[0])
