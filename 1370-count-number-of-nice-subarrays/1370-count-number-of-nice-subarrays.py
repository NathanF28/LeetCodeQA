class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        res = 0
        count = 0
        l,m = 0,0
        for r in range(len(nums)):
            if nums[r] % 2:
                count+=1
            while count > k:
                if nums[l] % 2:
                    count-=1
                l+=1
                m = l
            if count == k:
                while not nums[m] % 2:
                    m+=1
                res += (m-l)+1
        return res                        
        