class Solution:
    def maxAdjacentDistance(self, nums: List[int]) -> int:
        _max = 0
        for i in range(len(nums)):
            next = (i + 1 + len(nums)) % len(nums)
            _max = max(_max,abs(nums[i]-nums[next]))
        return _max
        