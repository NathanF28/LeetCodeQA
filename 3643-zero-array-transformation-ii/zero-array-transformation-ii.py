class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        l = 0
        r = len(queries)  - 1
        def validate(n):
            arr = [0] * (len(nums) +  1)
            print(arr,n)
            for query in queries[:n+1]:
                arr[query[0]]+= query[2]
                arr[query[1]+1]-= query[2]
            for i in range(1,len(arr)):
                arr[i] += arr[i-1]
            print(arr)
            for i in range(len(nums)):
                if nums[i] > arr[i]:
                    return False
            return True
        if not validate(r):
            return -1
        if set(nums) == {0}:
            return 0
        while l < r:
            mid = (l+r) // 2
            if validate(mid):
                r = mid
            else:
                l = mid + 1
        return l+1