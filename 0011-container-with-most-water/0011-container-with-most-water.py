class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0
        r = len(height)-1
        nums= height
        area = -float('inf')
        while l < r:
            width = r-l
            high = min(nums[l],nums[r])
            area = max(area,high*width)
            if nums[l] < nums[r]:
                l+=1
            else:
                r-=1
        return area            
        