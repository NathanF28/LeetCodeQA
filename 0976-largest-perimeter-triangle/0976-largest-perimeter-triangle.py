class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        
        nums.sort()
        while len(nums) > 2 and nums[0] >= nums[1] + nums[2]:
            nums.pop(0)
        return 0 if len(nums) < 3 else sum(nums[:3])