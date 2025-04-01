class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        heaters.sort()
        _max = 0
        for house in houses:
            if house in heaters:
                continue
            bl = bisect_left(heaters,house)
            if bl == 0:
                left = float('inf')
            else:
                left = bl - 1
            if bl == len(heaters):
                right = float('inf')
            else:
                right = bl
            r_d = heaters[right] - house if right != float('inf') else right
            l_d = house - heaters[left] if left != float('inf')   else left
            _max = max(_max, min(r_d,l_d))
        return _max