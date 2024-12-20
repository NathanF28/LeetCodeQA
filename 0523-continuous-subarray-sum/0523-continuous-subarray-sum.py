class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        if len(nums) < 2:
            return False
        sume = 0  
        map = {0: -1}
        for i in range(len(nums)):
            sume+= nums[i]
            if sume%k not in map:
                map[sume%k] = i
            else:
                if i-map[sume%k] > 1:
                    print(i,map)
                    return True           
        return False               
        