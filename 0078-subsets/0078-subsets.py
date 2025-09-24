class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        subsets = []

        def pick(index,path):
            if index == len(nums):
                subsets.append(path[:])
                return

            path.append(nums[index])
            pick(index+1,path)
            path.pop()
            pick(index+1,path)
        pick(0,[])
        return subsets