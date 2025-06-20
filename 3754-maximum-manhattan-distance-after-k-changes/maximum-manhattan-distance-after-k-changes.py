class Solution:
    def maxDistance(self, s: str, k: int) -> int:
        points = ["SW","NW","SE","NE"]

        _max = 0
        for corner in points:
            dist = 0
            rem = k
            for d in s:
                if d in corner:
                    dist+=1
                else:
                    if rem > 0:
                        dist+=1
                        rem-=1
                    else:
                        dist-=1
                _max = max(_max,dist)
        return _max










        