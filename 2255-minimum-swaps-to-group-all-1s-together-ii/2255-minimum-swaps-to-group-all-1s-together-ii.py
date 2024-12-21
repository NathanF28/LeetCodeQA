class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        ones = nums.count(1)
        nums = nums + nums
        l = 0
        count = 0
        maxe = 0
        for r in range(len(nums)):
            if nums[r]:
                count+=1
            if r-l+1 > ones:
                count-=nums[l]
                l+=1
            maxe = max(maxe, count)
        return ones - maxe       
                

        