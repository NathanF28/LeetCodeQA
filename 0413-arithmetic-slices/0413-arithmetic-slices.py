class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        if len(nums)<3:
            return 0
        count = 0   
        res = 0 
        for i in range(1,len(nums)-1):
            if nums[i+1] - nums[i] == nums[i] - nums[i-1]:
                print(i)
                count+=1
            else:
                count = 0
            res+=count   
        return res      

        