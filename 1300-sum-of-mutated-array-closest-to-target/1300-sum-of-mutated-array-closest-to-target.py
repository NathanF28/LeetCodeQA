class Solution:
    def findBestValue(self, arr: List[int], target: int) -> int:
        arr.sort()
        val = float('inf')
        od = float('inf')
        
        for i in range(arr[-1] + 1):
            pos = bisect_left(arr, i)
            sume = sum(arr[:pos]) + (len(arr) - pos) * i
            diff = abs(target - sume)
            
            if diff < od:
                od = diff
                val = i
            elif diff == od:
                val = min(val, i)
            else:
                break
        
        return val
