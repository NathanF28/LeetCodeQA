class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        lower = []
        middle = []
        bigger = []
        for num in nums:
            print(num)
            if int(num) < pivot:
                lower.append(num)
            elif int(num) == pivot:
                middle.append(num)
            else:
                bigger.append(num)
        for num in middle:
            lower.append(num)
        for num in bigger:
            lower.append(num)
        return lower