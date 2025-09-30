class Solution:
    def findBestValue(self, arr: List[int], target: int) -> int:
        arr.sort()
        initial_val = float('inf')
        initial_diff = initial_val

        l = 0
        r = arr[-1]
        prefix = arr.copy()
        for i in range(1, len(prefix)):
            prefix[i] += prefix[i-1]
        
        while l <= r:
            mid = (l+r)//2

            pos = bisect_left(arr,mid)
            sume = (prefix[pos-1] if pos > 0 else 0) + (len(arr)-pos) * mid
            diff = abs(sume - target)

            if diff < initial_diff or (diff == initial_diff and mid < initial_val):
                initial_diff = diff
                initial_val = mid
 
            if sume >= target:
                r = mid -1
            else:
                l = mid + 1
        return initial_val

        
