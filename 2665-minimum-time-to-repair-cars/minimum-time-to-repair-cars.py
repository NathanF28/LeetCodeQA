class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        l = 1
        r = max(ranks) *  cars * cars

        def validate(num):
            count = 0
            for rank in ranks:
                check = num / rank
                count+= int(check ** 0.5)
            return count >= cars

        while l < r:
            mid = (l+r)//2
            if validate(mid):
                r = mid
            else:
                l = mid + 1
        return l

        