class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        nums.sort()
        count = 0
        prev = [0]*len(nums)
        next = [0]*len(nums)
        for i in range(len(nums)):
            prev[i] = lower - nums[i] 
            next[i] = upper - nums[i] 
            bl = bisect_left(nums,prev[i],i+1,len(nums))
            bu = bisect_right(nums,next[i],i+1,len(nums))
            count+= bu-bl
        return count