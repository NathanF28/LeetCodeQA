class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        total = sum(nums)
        prefix = 0 
        count = 0
        for i in range(len(nums)-1):
            prefix+=nums[i]
            if prefix >= total - prefix:
                count+=1
                print(prefix,total-prefix)
                print(i)
        return count                 