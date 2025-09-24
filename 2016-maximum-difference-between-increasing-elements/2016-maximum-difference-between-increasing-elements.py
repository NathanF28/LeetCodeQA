class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        res =  -1
        _min = nums[0]
        for i in range(1,len(nums)):
            _min = min(_min,nums[i])
            if nums[i] > _min:
                res = max(res, nums[i] -  _min)
        return res
        