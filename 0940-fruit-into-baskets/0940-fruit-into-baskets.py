class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        map = {}
        l = 0
        res = 0
        for r in range(len(fruits)):
            if fruits[r] not in map:
                map[fruits[r]] = 1
            else:
                 map[fruits[r]] += 1
            while l < r and len(map) > 2:
                if map[fruits[l]] > 1:
                    map[fruits[l]]-=1
                else:
                    del map[fruits[l]]
                l+=1
            res = max(res, r-l+1)
        return res                     

        