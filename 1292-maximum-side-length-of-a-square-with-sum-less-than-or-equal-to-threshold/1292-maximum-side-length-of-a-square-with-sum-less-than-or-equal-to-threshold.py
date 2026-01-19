class Solution:
    def maxSideLength(self, mat: List[List[int]], threshold: int) -> int:
        m, n = len(mat), len(mat[0])

        pref = [[0] * (n+1) for _ in range(m+1)]    

        for i in range(m):      
            for j in range(n):
                pref[i+1][j+1] = pref[i+1][j] + pref[i][j+1] - pref[i][j] + mat[i][j]


        def check(x):
            return any((pref[i + x][j + x] - pref[i][j + x] - pref[i + x][j] + pref[i][j]) <= threshold for i in range(m - x + 1) for j in range(n - x + 1))

        low, high = 1, min(m,n)
        while low <= high:
            mid = (low + high) // 2
            
            if check(mid):
                low = mid + 1
            else:
                high = mid - 1

        return high