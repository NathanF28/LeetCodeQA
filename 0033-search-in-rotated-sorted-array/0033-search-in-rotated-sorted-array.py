class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left < right:
            if nums[left] == target or nums[right] == target:
                return left

            mid = (left + right) // 2
            # Left portion
            if nums[left] <= nums[mid]:
                if nums[left] < target:
                    right = mid - 1
                else:
                    left = mid + 1

            # Right Portion
            elif nums[left] > nums[mid]:
                if nums[right] < target:
                    right = mid - 1
                else:
                    left = mid + 1


        return left if nums[left] == target else -1
