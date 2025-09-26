class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        count = 0 
        nums.sort()
        for i in range(len(nums)-2):
            for j in range(i+1, len(nums)-1):
                sume = nums[i] + nums[j]
                k = bisect_left(nums, sume, j + 1, len(nums))
                count += k - j - 1
        return count

