class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        z = 0
        l = 0
        _max = 0
        for r in range(len(nums)):
            if not nums[r]:
                z+=1
            while l<r and z > 1:
                if nums[l] == 0:
                    z-=1
                l+=1
            _max = max(_max,r-l)
        return _max
            
        