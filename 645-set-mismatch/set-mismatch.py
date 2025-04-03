class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        nums.sort()
        map = Counter(nums)
        i = 1
        res = []
        for key,value in map.items():
            if value > 1:
                res.append(key)
       
        for i in range(1,len(nums)+1):
            if i not in map:
                res.append(i)
        return res