class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        index_map = {}
        for index,num in enumerate(nums2):
            if num not in index_map:
                index_map[num] = index
        liste = []        
        for num in nums1:
            r = index_map[num]
            while True:
                if r == len(nums2):
                    liste.append(-1)
                    break
                if nums2[r] > num: 
                    liste.append(nums2[r])
                    break
                
                r+=1    
        return liste                       
        