class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:

        def merge(nums):
            if len(nums) == 1:
                return nums
            mid = (len(nums))//2
            left = merge(nums[:mid])
            right = merge(nums[mid:])
            return combine(left,right)
        def combine(list1,list2):
            l = 0 
            r = 0
            final = []
            while l < len(list1) and r < len(list2):
                if list1[l] < list2[r]:
                    final.append(list1[l])
                    l+=1
                else:
                    final.append(list2[r])
                    r+=1
            if r < len(list2):
                final.extend(list2[r:])
            else:
                final.extend(list1[l:])
            return final
        return merge(nums) 