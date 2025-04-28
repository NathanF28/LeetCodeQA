class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        l = 0
        _sum = 0
        count = 0
        for r in range(len(nums)):
            _sum+= nums[r]
            while l <= r and (_sum * (r-l +1))  >= k:
                _sum-=nums[l]
                l+=1
            if (_sum * (r-l +1)) < k:
                count+= r-l+1
        return count

        