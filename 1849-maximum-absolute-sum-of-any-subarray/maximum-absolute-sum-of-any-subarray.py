class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        max_pre,min_pre = 0,0
        prefix = 0
        res = 0
        for num in nums:
            prefix+= num
            res = max(res,abs(prefix-max_pre),abs(prefix-min_pre))
            max_pre = max(prefix,max_pre)
            min_pre = min(prefix,min_pre)
        return res
        