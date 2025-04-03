class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:


        def mergeSort(array):
            if len(array) == 1:
                return array
            mid = len(array)//2
            left = mergeSort(array[:mid])
            right = mergeSort(array[mid:])
            return merge_lists(left,right)

        def merge_lists(left,right):
            res = []
            first = 0
            second = 0

            while first < len(left) and second < len(right):
                if left[first] <= right[second]:
                    res.append(left[first])
                    first+=1
                else:
                    res.append(right[second])
                    second+=1
            
            res.extend(left[first:])
            res.extend(right[second:])
            return res
        x = mergeSort(nums)
        return x