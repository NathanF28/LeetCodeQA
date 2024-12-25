class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l = 1
        r = 1
        while r < len(nums):
            print(r,l)
            if nums[r] != nums[l-1]:
                nums[l],nums[r] = nums[r],nums[l]
                l+=1
            r+=1    
        return l

        