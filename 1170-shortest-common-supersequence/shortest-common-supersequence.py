class Solution:
    def shortestCommonSupersequence(self, s: str, t: str) -> str:
        n, m = len(s), len(t)
        dp = [[0] * (m + 1) for _ in range(n + 1)]

        for j in range(m):
            dp[n][j] = m - j
        
        for i in range(n - 1, -1, -1):
            dp[i][m] = n - i
            for j in range(m - 1, -1, -1):
                if s[i] == t[j]:
                    dp[i][j] = 1 + dp[i + 1][j + 1]
                else:
                    dp[i][j] = 1 + min(dp[i + 1][j], dp[i][j + 1])
        
        res = ""
        i = j = 0
        while i < n and j < m:
            if s[i] == t[j]:
                res += s[i]
                i += 1
                j += 1
            elif dp[i + 1][j] <= dp[i][j + 1]:
                res += s[i]
                i += 1
            else:
                res += t[j]
                j += 1
        
        return res + s[i:] + t[j:] 