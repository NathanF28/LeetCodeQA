class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k <= 1:
            return 0
        prefix = 1
        count = 0
        l = 0
        for r in range(len(nums)):
            prefix*=nums[r]
            while l < r and prefix >= k:
                prefix//=nums[l]
                l+=1
            if prefix < k:
                count+=r-l+1
        return count        

        