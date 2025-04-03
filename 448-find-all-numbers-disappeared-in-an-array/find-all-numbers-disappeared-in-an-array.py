class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        check = set(nums)
        i = 1
        res = []
        for i in range(1,len(nums)+1):
            if i not in check:
                res.append(i)
            i+=1
        return res

