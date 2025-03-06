class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = [0]
        map = {}
        for i in range(1,len(nums2)):
            while stack and nums2[i] > nums2[stack[-1]]:
                map[nums2[stack.pop()]] = i
            stack.append(i)
        liste = []
        for num in nums1:
            if num not in map:
                liste.append(-1)
            else:
                liste.append(nums2[map[num]])
        return liste

            


                

