class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        map = {}
        def backtrack(sume,path,target):
            if sume == target:
                check = tuple(sorted(path))
                if check not in map:
                    map[check]=1
                    res.append(path[:])
                return
            if sume > target:
                return
            for i in range(len(nums)):
                sume+=nums[i]
                path.append(nums[i])
                backtrack(sume,path,target)
                sume-=nums[i]
                path.pop()
        backtrack(0,[],target)
        liste = []
        if len(res) == 0:
            return []
        return  res 