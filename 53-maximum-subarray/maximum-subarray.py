class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        l = 0 
        curr = 0
        _max = -float('inf')
        for i in range(len(nums)):
            if curr + nums[i] < nums[i]:
                l = i
                curr = 0
            curr+= nums[i]
            _max = max(_max, curr)
        return _max

