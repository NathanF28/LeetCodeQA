class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        nums.sort()
        l = 0
        count = 0
        while l < len(nums):
            cap = nums[l] + k
            r = l
            while r < len(nums) and nums[r] <= cap:
                r+=1
            l = r
            count+=1
        return count
