class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        map = {}
        count = 0
        l = 0
        val = len(set(nums))
        for r in range(len(nums)):
            if nums[r] not in map:
                map[nums[r]] =  1
            else:
                map[nums[r]] +=1
            while len(map) == val:
                count+=len(nums)-r
                if map[nums[l]]>1:
                    map[nums[l]]-=1
                else:
                    del map[nums[l]]
                l+=1
        return count                


        