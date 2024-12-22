class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        map = {0:-1}
        prefix = 0 
        for i in range(len(nums)):
            prefix+=nums[i]
            rem = prefix%k
            if rem not in map:
                map[rem] = i
            else:
                if i - map[rem] > 1:
                    return True
        return False            
        