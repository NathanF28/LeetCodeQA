class Solution:
    def minOperations(self, nums: List[int]) -> int:
        count = 0
        for i in range(len(nums)-2):
            if nums[i] == 0:
                nums[i] = 1
                if nums[i+1] == 1:
                    nums[i+1] = 0
                else:
                    nums[i+1] = 1
                if nums[i+2] == 1:
                    nums[i+2] = 0
                else:
                    nums[i+2] = 1
                count+=1
        return count if len(nums) == sum(nums) else -1
        