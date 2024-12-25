class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l = 0
        res = 0
        count = 0
        for r in range(len(nums)):
            if nums[r] == 1:
                count+=1
            while l<= r and r-l+1 - count > k:
                if nums[l]:
                    count-=1
                l+=1
            res = max(r-l+1,res)
        return res            


        