class Solution:
    def numTilings(self, n: int) -> int:
        MOD = 10 ** 9 + 7
        memo = {}
        def recursion(n):
            if n in memo:
                return memo[n]
            if n == 1:
                return 1
            if n == 2:
                return 2
            if n == 3:
                return 5
            if n == 4:
                return 11
            x = recursion(n-1) * 2 + recursion(n-3) 
            memo[n] = x
            return x
        return recursion(n) % MOD
    
            