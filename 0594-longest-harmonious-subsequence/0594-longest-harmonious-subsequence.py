class Solution:
    def findLHS(self, nums: List[int]) -> int:
        nums = sorted(nums)
        print(nums)

        l = 0
        res = 0


        for r in range(len(nums)):
            if abs(nums[r] - nums[l]) >= 2:
                print(r,l)                 
                l+=1
            if nums[r] == nums[l]+1:
                res = max(r-l+1,res)       
        return res         

           
                 
        