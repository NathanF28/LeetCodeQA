class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k <=1:
            return 0
        l = 0
        prefix = 1
        count = 0
        for r in range(len(nums)):
            prefix*=nums[r]
            while l< len(nums) and prefix >= k:
                prefix//= nums[l]
                l+=1
            count+= r-l+1
        return count    

        