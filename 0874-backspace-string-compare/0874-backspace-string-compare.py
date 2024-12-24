class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stack1 = []
        for let in s:
            if stack1 and let == "#":
                stack1.pop()
            elif let!= "#":
                stack1.append(let)
        stack2 = []
        for let in t:
            if stack2 and let == "#":
                stack2.pop()
            elif let!= "#":
                stack2.append(let)
        print(stack1,stack2)        
        return stack1 == stack2        

