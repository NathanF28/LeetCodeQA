class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        l = max(nums)
        r = sum(nums)

        def validate(num):
            splits = k
            res = nums[0]
            count = 0
            for i in range(1,len(nums)):
                if res + nums[i] > num:
                    count+=1
                    res = 0
                res+= nums[i]
            return count+1 <= splits    

        while l <= r:
            mid = (l+r)//2
            if validate(mid):
                r = mid - 1
            else:
                l = mid +1
        return l

        