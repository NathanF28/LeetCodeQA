class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        last = float('inf')
        for i in range(len(nums)):
            if nums[i]:
                if last == float('inf'):
                    last = i
                    continue
                if i - last - 1 < k:
                    return False
                last = i
        return True