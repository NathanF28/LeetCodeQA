class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        inv = -1
        minPos = -1
        maxPos = -1
        count = 0
        for i in range(len(nums)):
            if nums[i] < minK or nums[i] > maxK:
                inv = i
            if nums[i] == minK:
                minPos = i
            if nums[i] == maxK:
                maxPos = i
            beginning = min(minPos,maxPos)
            count+= max(0, beginning - inv)
        return count 

        
        