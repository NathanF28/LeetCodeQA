class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        def binary():
            l = 0
            r = len(matrix) - 1

            
            while l <= r:
                mid = (l+r)//2
                if matrix[mid][0] > target:
                    r = mid - 1
                else:
                    l = mid + 1
            
            return max(l - 1,0)

        x = binary()
        l = 0
        r = len(matrix[x]) - 1
        while l <= r:
            mid = (l+r)//2
            if matrix[x][mid] > target:
                r = mid - 1
            elif matrix[x][mid] < target :
                l = mid + 1
            else:
                return True
        return False


