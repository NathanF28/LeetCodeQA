from collections import Counter
from typing import List

class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        # Step 1: Find the dominant element
        whole = Counter(nums)
        dominant, count = max(whole.items(), key=lambda x: x[1])  # Element with max frequency
        
        # Step 2: Check if it's actually dominant
        if count * 2 <= len(nums):  
            return -1  # No dominant element

        part = Counter()
        left_count = 0  # Count of dominant element in left part
        
        # Step 3: Iterate and find the minimum split index
        for i in range(len(nums)):
            part[nums[i]] += 1
            whole[nums[i]] -= 1
            left_count += (nums[i] == dominant)

            # Check if dominant remains dominant in both parts
            if (left_count * 2 > (i + 1)) and (whole[dominant] * 2 > (len(nums) - i - 1)):
                return i  # Smallest valid index
        
        return -1  # No valid split found
 
        