class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        map = {}
        prefix = 0
        maxe = -float('inf')
        for r in range(len(nums)):            
            need = nums[r]+k
            neg = nums[r]-k
            
            if need not in map:
                map[need] = prefix
            else:
                map[need] = min(map[need],prefix)

            if neg not in map:    
                map[neg] = prefix
            else:
                map[neg] = min(map[neg],prefix)    

            if nums[r] in map:
                sume = prefix - map[nums[r]] + nums[r] 
                print(sume)
                maxe = max(maxe,sume)
            prefix+=nums[r]   
        return maxe if maxe != -float('inf') else 0  






        