class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        longest = 1
        l = 0
        curr = 0
        for r in range(len(nums)):
            while curr & nums[r]:
                curr ^= nums[l]
                l+=1
            curr |= nums[r]
            longest = max(r-l+1,longest)
        return longest
        