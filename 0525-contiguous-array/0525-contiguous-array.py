class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        count = 0
        map = {0:-1}
        res = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                count+=1
            else:
                count-=1
            if count not in map:
                map[count] = i    
            else:
                res = max(i - map[count],res) 
        return res               

        