class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        for op in operations:
            if op == "C":
                if stack:
                    stack.pop()
            elif op == "D":
                if stack:
                    ans = int(stack[-1])
                    stack.append(2*ans)
                    print(stack)
            elif op == "+":
                if stack:
                    first = int(stack.pop())
                    second = int(stack[-1])
                    stack.append(first)
                    stack.append(first+second)
            else:
                stack.append(int(op))
        print(stack)        
        return sum(stack)                


        