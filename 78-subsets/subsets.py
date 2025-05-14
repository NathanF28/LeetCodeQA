class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        power = []
        for mask in range (1 << len(nums)):
            subsets = []
            for i in range(len(nums)):
                if mask & (1 << i):
                    subsets.append(nums[i])
            power.append(subsets)
        return power
