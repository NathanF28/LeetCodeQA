from sortedcontainers import SortedList
class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], diff: int) -> int:
        arr = []
        arr.append(nums1[-1]-nums2[-1])
        arr = SortedList(arr)
        count = 0 
        for i in range(len(nums1)-2,-1,-1):
            search = nums1[i]-nums2[i]-diff
            bl = bisect_left(arr,search)
            count+= len(arr) - bl
            arr.add(nums1[i]-nums2[i])
        return count


        