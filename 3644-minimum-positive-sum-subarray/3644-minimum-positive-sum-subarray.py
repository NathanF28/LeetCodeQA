class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        res = float('inf')
        for k in range(l,r+1):
            print(k)
            left = 0
            prefix = 0
            for right in range(len(nums)):
                prefix+=nums[right]
                if right-left+1 == k:
                    if prefix > 0:
                        res = min(prefix,res)
                    prefix-=nums[left]
                    left+=1
        return res if res != float('inf') else -1           



        