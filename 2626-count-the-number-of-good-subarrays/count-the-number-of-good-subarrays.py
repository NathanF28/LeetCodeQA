class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        l = 0
        map = {}
        count = 0
        res = 0
        for r in range(len(nums)):
            if nums[r] not in map:
                map[nums[r]] = 1
            else:
                count+=map[nums[r]]
                map[nums[r]] += 1
            while count >= k:
                res+= len(nums)-r
                if map[nums[l]] > 1:
                    count-= map[nums[l] ]-1
                    map[nums[l]]-=1
                else:
                    del map[nums[l]]
                l+=1
        return res


            


        