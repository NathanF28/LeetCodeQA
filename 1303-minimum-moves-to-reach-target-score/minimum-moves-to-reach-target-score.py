class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        count = 0
        while maxDoubles > 0 and target > 1:
            if target % 2 == 1:
                count+=1
            maxDoubles-=1
            target //=2
            count+=1
            print(target,count,maxDoubles)
        return count + target - 1
        