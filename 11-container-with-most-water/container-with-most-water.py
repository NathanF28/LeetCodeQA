class Solution:
    def maxArea(self, nums: List[int]) -> int:
        area = 0
        l = 0
        r = len(nums)-1
        while l < r:
            check = min(nums[l],nums[r]) * (r-l)
            area = max(area,check)
            if nums[l] < nums[r]:
                l+=1
            else:
                r-=1
        return area
        