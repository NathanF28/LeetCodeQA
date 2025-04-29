class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        _max = max(nums)
        l = 0
        count = 0
        _max_count = 0
        for r in range(len(nums)):
            if nums[r] == _max:
                _max_count +=1
            while l <= r and _max_count == k:
                count+= len(nums)-r
                if nums[l] == _max:
                    _max_count -=1
                l+=1
        return count

        