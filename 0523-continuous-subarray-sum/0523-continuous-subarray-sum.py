class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        map = {0:-1}
        sume = 0 
        for index,num in enumerate(nums):
            sume+=num
            rem = sume%k
            if rem not in map:
                map[rem] = index
            else:
                if index - map[rem] > 1:
                    return True
        return False                  
        