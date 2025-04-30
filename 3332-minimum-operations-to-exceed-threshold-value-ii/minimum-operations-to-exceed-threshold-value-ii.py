import heapq
class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        count = 0
        while len(nums) > 1: 
            if nums[0] >= k:
                break
            x = heappop(nums)
            y = heappop(nums)
            val = min(x,y) * 2 + max(x,y)
            heappush(nums,val)
            count+=1
        return count

        
