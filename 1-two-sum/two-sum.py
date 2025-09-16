class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}

        for i in range(len(nums)):
            need = target - nums[i]
            if need in map:
                return [map[need],i]
            map[nums[i]] = i
        