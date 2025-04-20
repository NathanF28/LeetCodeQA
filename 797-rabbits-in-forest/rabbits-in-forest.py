class Solution:
    def numRabbits(self, numwers: List[int]) -> int:
        map = {}
        count = 0
        for num in numwers:
            if num+1 not in map:
                count+= num+1
                map[num+1] = num
            else:
                if map[num+1] == 0:
                    del map[num+1]
                    count+= num+1
                    map[num+1] = num
                else:
                    map[num+1]-=1
        return count
        