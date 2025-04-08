class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        map = Counter(nums)
        count = 0
        i = 0
        while i < len(nums):
            if sum(map.values()) == len(map):
                return count
            fur = min(i+3,len(nums))
            check = Counter(nums[i:fur])
            map-=check
            count+=1
            i+=3
        return count
            