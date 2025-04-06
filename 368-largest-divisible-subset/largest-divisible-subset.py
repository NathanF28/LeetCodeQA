class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        memo = {}
        def dfs(index):
            if index == len(nums):
                return []
            if index in memo:
                return memo[index]
            res = [nums[index]] 
            for j in range(index+1,len(nums)):
                if nums[j] % nums[index] == 0:
                    temp = [nums[index]] + dfs(j)
                    if len(temp) > len(res):
                        res = temp
            memo[index] = res
            return res
        longest = dfs(0)
        for i in range(1,len(nums)):
            if len(dfs(i)) > len(longest):
                longest = dfs(i)
        return longest


        