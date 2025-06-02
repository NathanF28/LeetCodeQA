class Solution:
    def maxSubArray(self, nums: List[int]) -> List[int]:
        
        def merge(nums,l,r):
            if l == r:
                return nums[l]
            mid = (l+r)//2 
            left = merge(nums,l,mid)
            right = merge(nums,mid+1,r)
            cross = best_mid(nums,l,mid,r)
            return max(left,right,cross)

        def best_mid(nums,start,mid,end):
            left_best = float('-inf')
            tot = 0
            for i in range(mid,start-1,-1):
                tot+=nums[i]
                left_best = max(left_best,tot)
            right_best = float('-inf')
            tot = 0
            for i in range(mid+1,end+1):
                tot+=nums[i]
                right_best = max(right_best,tot)
            return left_best + right_best
        return merge(nums,0,len(nums)-1)
