class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        middle = float('-inf')
        stack = []
        for num in nums[::-1]:
            if num <middle:
                return True
            while stack and num > stack[-1]:
                middle = stack.pop()
            stack.append(num)
        return False

        
        