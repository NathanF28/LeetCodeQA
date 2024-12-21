class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        prefix = 0
        total = sum(nums)
        for i in range(len(nums)):
            if prefix == total - prefix - nums[i]:
                return i
            prefix+=nums[i]
        return -1    
        