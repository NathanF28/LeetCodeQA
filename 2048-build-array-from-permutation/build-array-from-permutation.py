class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        arr = nums.copy()
        for i in range(len(nums)):
            arr[i] = nums[nums[i]]
        return arr
        