class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}
        for i in range(len(nums)):
            need = target - nums[i]
            if need not in map:
                map[nums[i]] = i
            else:
                return [map[need],i]         