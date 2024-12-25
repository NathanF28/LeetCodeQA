class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        l =  0
        res= 0
        nums = fruits
        map = {}
        for r in range(len(fruits)):
            if nums[r] not in map:
                map[nums[r]] = 1
            else:
                map[nums[r]] +=1
            while len(map) > 2:
                if map[nums[l]] > 1:
                    map[nums[l]]-=1 
                else:
                    del map[nums[l]]
                l+=1
            res = max(res,r-l+1)
        return res                        

        