class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        n = original 
        while  n in nums:
            n = 2 * n
        return n