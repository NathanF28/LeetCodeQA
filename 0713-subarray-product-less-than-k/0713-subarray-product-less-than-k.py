class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        l = 0
        count = 0
        prefix =1
        for r in range(len(nums)):
            prefix*=nums[r]
            print(prefix)
            while l < r and prefix >= k:
                prefix//= nums[l]
                l+=1
            if prefix < k:
                print(prefix,r,l)
                count+=r-l+1
        return count              

        