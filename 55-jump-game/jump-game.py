class Solution:
    def canJump(self, nums: List[int]) -> bool:
        possible = len(nums) -1
        for i in range(len(nums)-1, -1,-1):
            if i + nums[i] >= possible:
                possible = i
        return possible == 0

        