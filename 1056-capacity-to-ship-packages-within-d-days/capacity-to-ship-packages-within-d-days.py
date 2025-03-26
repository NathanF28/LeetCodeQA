class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l = max(weights)
        r = sum(weights)
        def possible(num):
            count = 1 
            _sum = 0
            for weight in weights:
                if weight + _sum > num:
                    _sum = 0
                    count+=1
                _sum+= weight 
            return count <= days 
        while l < r:
            mid = (l+r) // 2
            if possible(mid):
                    r = mid
            else:
                l = mid + 1
        return l 