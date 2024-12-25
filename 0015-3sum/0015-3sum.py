class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        res = []
        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue

            l,r = i+1, len(nums)-1
            need = -nums[i]
            while l< r:
                sume = nums[l] + nums[r]    
                if sume > need:
                    r-=1
                elif sume < need:
                    l+=1
                else:
                    res.append([nums[i],nums[l],nums[r]])
                    l+=1
                    r-=1
                    while l < r and nums[l] == nums[l-1]:
                        l+=1
        return res                        
        