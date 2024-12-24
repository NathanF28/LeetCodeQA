class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        map = {0:1}
        prefix = 0
        count = 0
        l = 0
        for r in range(len(nums)):
            prefix+=nums[r]
            need = prefix - k 
            if need in map:
                count+=map[need]
            if prefix not in map:
                map[prefix] = 1
            else:
                map[prefix]+=1    
            
        return count        



        