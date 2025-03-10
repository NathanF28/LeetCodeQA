class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        l = 0
        maxq = deque()
        minq = deque()
        maximum = 0
        for i in range(len(nums)):
            while maxq and nums[i] > maxq[-1]:
                maxq.pop()
            maxq.append(nums[i]) 
            while minq and nums[i] < minq[-1]:
                minq.pop()
            minq.append(nums[i]) 
            while maxq and minq and maxq[0] - minq[0] > limit:
                if nums[l] == maxq[0]:
                    maxq.popleft()
                if nums[l] == minq[0]:
                    minq.popleft()
                l+=1
            maximum = max(maximum,i-l+1)
        return maximum
            