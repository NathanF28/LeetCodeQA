class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        def find(direction):
            l = 0
            r = len(nums) -1
            while l <= r:
                mid = (l+r)//2
                if nums[mid] > target:
                    r = mid -1
                elif nums[mid] < target:
                    l= mid + 1
                else:
                    if direction == "left":
                        if mid == 0:
                            return 0
                        elif nums[mid-1] != target:
                            return mid
                        else:
                            r = mid-1
                    else:
                        if mid == len(nums) - 1:
                            return mid
                        elif nums[mid+1] != target:
                            return mid
                        else:
                            l = mid + 1
            return -1
        left = find("left")
        right = find("right")
        return left,right


        
        