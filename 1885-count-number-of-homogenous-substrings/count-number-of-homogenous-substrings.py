class Solution:
    def countHomogenous(self, nums: str) -> int:
        MOD = 10 ** 9 + 7
        l = 0
        count=0
        res = 0
        for r in range(len(nums)):
            if nums[r] != nums[l]:
                res += (count * (count+1))//2
                l = r
                count = 0
            count+=1
        res += (count*(count+1))//2
        return res % MOD
            
            

