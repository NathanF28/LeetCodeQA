class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        longest = 0
        map = {0:-1}
        prefix = 0
        for i,nums in enumerate(nums):
            if nums:
                prefix+=1
            else:
                prefix-=1
            if prefix not in map:
                map[prefix] = i
            else:
                longest = max(longest, i-map[prefix])
        return longest
            
        