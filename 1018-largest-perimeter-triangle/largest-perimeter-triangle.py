class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        p = 0
        nums.sort()
        for i in range(len(nums)-1,1,-1):
            r = i-1
            l = i-2 
            sume = nums[i] + nums[l] + nums[r]
            if nums[i] < nums[l] + nums[r]:
                p = max(p, sume)
        return p 

        