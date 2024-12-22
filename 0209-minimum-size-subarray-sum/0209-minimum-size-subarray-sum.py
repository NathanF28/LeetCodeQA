class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        maximum = float('inf')
        prefix = 0
        l = 0
        for r in range(len(nums)):
            prefix+=nums[r] 
            while prefix >= target:
                maximum = min(maximum,r-l+1)
                prefix-= nums[l]
                l+=1
               
        return maximum if maximum != float('inf') else 0       
        