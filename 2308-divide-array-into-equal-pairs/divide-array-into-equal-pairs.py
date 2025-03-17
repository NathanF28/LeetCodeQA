class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        check = list(set(nums))
        map = Counter(nums)
        for num in check:
            if map[num] % 2 == 1:
                return False
        return True 