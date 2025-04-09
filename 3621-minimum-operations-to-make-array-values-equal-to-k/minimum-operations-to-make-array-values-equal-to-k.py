class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        if k > min(nums):
            return -1
        return len(set(nums)) - bisect_right(sorted(set(nums)),k)
        