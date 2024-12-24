class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = ["+","-","*","/"]
        for val in tokens:
            if val in operators:
                a = int(stack.pop())
                b = int(stack.pop())
                if val == "+":
                    stack.append(a+b)
                elif val == "-":
                    stack.append(b-a) 
                elif val == "*":
                    stack.append(a*b) 
                elif val == "/":
                    stack.append(int(b/a))
            else:
                stack.append(int(val))
        return stack.pop()                 
        