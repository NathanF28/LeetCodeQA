class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        max_sum = 0
        prefix = 0
        map = {}
        l = 0
        for r in range(len(nums)):
            prefix+= nums[r]
            if nums[r] not in map:
                map[nums[r]] = 1
            else:
                map[nums[r]] += 1
            if r-l+1 == k:
                if len(map) == k:
                    max_sum = max(max_sum,prefix)
                if map[nums[l]] == 1:
                    del map[nums[l]]
                else:
                    map[nums[l]]-=1
                prefix-=nums[l]    
                l+=1  
                
        return max_sum                       

        