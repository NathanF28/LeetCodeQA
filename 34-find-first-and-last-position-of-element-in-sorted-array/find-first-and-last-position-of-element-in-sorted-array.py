class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        def binSearch(direction):
            l = 0
            r = len(nums) - 1
            i = -1
            while l <= r:
                mid = (l+r)//2

                if nums[mid] > target:
                    r = mid - 1
                elif nums[mid] < target:
                    l = mid + 1

                else:
                    i = mid
                    if direction == "left":
                        r = mid - 1
                    else:
                        l = mid + 1 
            return i

        l = binSearch("left") 
        r = binSearch("right") 
        return [l,r]