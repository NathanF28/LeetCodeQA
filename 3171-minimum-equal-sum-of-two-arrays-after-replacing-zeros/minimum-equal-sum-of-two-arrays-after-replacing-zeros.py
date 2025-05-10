class Solution:
    def minSum(self, nums1: List[int], nums2: List[int]) -> int:
        min_a = sum(nums1) + nums1.count(0)
        min_b = sum(nums2) + nums2.count(0)
        max_a = sum(nums1) if nums1.count(0) == 0 else float('inf')
        max_b = sum(nums2) if nums2.count(0) == 0 else float('inf')

        if min_a > max_b or min_b > max_a:
            return -1
        return max(min_a,min_b)