class Solution:
    def numberOfPaths(self, grid: list[list[int]], k: int) -> int:
        MOD = 10**9 + 7
        rows, cols = len(grid), len(grid[0])
        
        # dp[i][j][rem] = paths to (i,j) with sum % k == rem
        dp = [[[0] * k for _ in range(cols)] for _ in range(rows)]
        
        dp[0][0][grid[0][0] % k] = 1
        
        for i in range(rows):
            for j in range(cols):
                for rem in range(k):
                    if i > 0:
                        new_rem = (rem + grid[i][j]) % k
                        dp[i][j][new_rem] = (dp[i][j][new_rem] + dp[i-1][j][rem]) % MOD
                    if j > 0:
                        new_rem = (rem + grid[i][j]) % k
                        dp[i][j][new_rem] = (dp[i][j][new_rem] + dp[i][j-1][rem]) % MOD
        
        return dp[rows-1][cols-1][0]
