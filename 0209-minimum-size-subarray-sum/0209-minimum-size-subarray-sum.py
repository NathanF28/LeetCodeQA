class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        minimum =  float('inf')
        l = 0
        prefix = 0
        for r in range(len(nums)):
            prefix+=nums[r] 
            while prefix >= target:
                minimum = min(r-l+1,minimum)
                prefix-=nums[l]
                l+=1
                  
        if minimum != float('inf'):
            return minimum
        else:
            return 0               
            
        