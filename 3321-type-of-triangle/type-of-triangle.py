class Solution:
    def triangleType(self, nums: List[int]) -> str:
        if nums[0] >= nums[1] + nums[2] or nums[1] >= nums[0] + nums[2] or nums[2] >= nums[0] + nums[1]:
            return "none"

        map = {
            1 : "equilateral",
            2: "isosceles",
            3: "scalene"
        }
        return map[len(set(nums))]