class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        _max = 0
        prev_max = [-1] * len(nums)
        temp_max = nums[0]
        for i in range(1,len(nums)):
            temp_max = max(temp_max,nums[i-1])
            prev_max[i] = temp_max
        next_max = [-1] * len(nums)
        temp_max = nums[-1]
        for i in range(len(nums)-2,-1,-1):
            temp_max = max(temp_max,nums[i+1])
            next_max[i] = temp_max
        for i in range(1,len(nums)-1):
            _max = max((prev_max[i] - nums[i]) * next_max[i],_max)
        return _max