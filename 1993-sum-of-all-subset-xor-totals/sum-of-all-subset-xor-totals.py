class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:


        def backtrack(index,total):
            if index == len(nums):
                return total
            return backtrack(index+1,total) + backtrack(index+1,total^ nums[index])

        return backtrack(0,0)

        