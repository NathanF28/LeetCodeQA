class Solution:
    def canThreePartsEqualSum(self, arr: List[int]) -> bool:
        prefix = 0
        total = sum(arr)
        count = 0
        target =total//3
        if total % 3 !=  0:
            return False
        for i in range(len(arr)):
            prefix+=arr[i]
            if prefix == target:
                count+=1
                prefix = 0
            if count == 3:
                return True
        return False             
        