class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        res = -float('inf')
        l = 0
        prefix = 0
        for r in range(len(nums)):
            prefix+=nums[r]
            if r-l+1 == k:
                average = prefix/k
                res = max(average,res)
                prefix-=nums[l]
                l+=1
           
        return res        
        
        