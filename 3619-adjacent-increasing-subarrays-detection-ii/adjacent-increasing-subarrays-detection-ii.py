class Solution:
    def maxIncreasingSubarrays(self, nums: List[int]) -> int:
        def hasIncreasingSubarrays(nums, k):
            prev, cur, k2 = 0, 1, k*2
            for i in range(1, len(nums)):
                if nums[i-1] < nums[i]:
                    cur += 1
                else:
                    prev, cur = cur, 1
                if (cur >= k and prev >= k) or cur >= k2:
                    return True
            return False

        l = 0
        r = len(nums)//2

        while l <= r:
            mid = (l+r)//2
            if hasIncreasingSubarrays(nums,mid):
                l = mid + 1
            else:
                r = mid -1
        return r