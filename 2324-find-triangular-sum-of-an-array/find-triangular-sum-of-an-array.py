class Solution:
    def triangularSum(self, nums: List[int]) -> int:


        def recur(arr):
            if len(arr) == 1:
                return arr[0]
            newArr = []
            for i in range(1,len(arr)):
                newArr.append((arr[i]+arr[i-1])%10)
            return recur(newArr)
        return recur(nums)