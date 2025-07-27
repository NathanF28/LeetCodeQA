class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        v = 0
        h = 0 
        stack = []
        for num in nums:
            if stack and stack[-1] == num:
                continue
            stack.append(num)
        nums = stack
        for i in range(1,len(nums)-1):
            if nums[i] > nums[i-1] and nums[i] > nums[i+1]:
                h+=1
            elif nums[i] < nums[i-1] and nums[i] < nums[i+1]:
                v+=1
        return h+v
        