class Solution:
    def maxDistance(self, s: str, k: int) -> int:
        res = 1
        check = ["SW","SE","NE","NW"]
        for corner in check:
            final = 0
            chance = k
            for d in s:
                if d in corner:
                    final+=1
                else:
                    if chance > 0:
                        final+=1
                        chance-=1
                    else:
                        final-=1
                res = max(final,res)
        return res





