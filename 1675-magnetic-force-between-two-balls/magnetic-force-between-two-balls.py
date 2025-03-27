class Solution:
    def maxDistance(self, pos: List[int], m: int) -> int:
        l = 1
        r = max(pos) - min(pos)
        pos.sort()
        def validate(num):
            balls = m -1
            curr = 0
            for i in range(balls):
                next_pos = num + pos[curr]
                bl = bisect_left(pos,next_pos)
                if bl == len(pos):
                    return False
                curr = bl
            return True


        while l<=r:
            mid = (l+r)//2
            if validate(mid):
                l = mid+1
            else:
                r = mid -1
        return r
        
        