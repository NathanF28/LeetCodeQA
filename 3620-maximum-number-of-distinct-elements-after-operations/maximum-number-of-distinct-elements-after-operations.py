class Solution:
    def maxDistinctElements(self, nums: List[int], k: int) -> int:
        nums.sort()
        prev = -float('inf')
        d = 0
        for num in nums:
            target = prev + 1
            _min = num - k
            curr = max(_min,target)
            if curr <= num + k:
                prev = curr
                d+=1
        return d