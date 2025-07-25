class Solution:
    def maxSum(self, nums: List[int]) -> int:
        if max(nums) < 0:
            return max(nums)
        check = set()
        for num in nums:
            if num not in check and num >=0:
                check.add(num)
        return sum(list(check))