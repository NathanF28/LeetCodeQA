class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        invalid_start = -1     #left most bound, where it starts to be valid
        minPos = -1
        maxPos = -1
        count = 0
        for i in range(len(nums)):
            if nums[i] < minK or nums[i] > maxK:
                invalid_start = i   # this number can never be included in the array, it disrupts it so we mark it as the last surely invalid place
            if nums[i] == minK:
                minPos= i
            if nums[i] == maxK:
                maxPos= i
            count+= max(0,min(minPos,maxPos) - invalid_start) # min(minPos,maxPos) means where the valid subarray will start and the rest includes valid numbers between that place and invalid_start
            # max(0, ...) is if invalid_start is larger 
        return count