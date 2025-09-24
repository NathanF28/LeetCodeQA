class Solution:
    def fib(self, n: int) -> int:
        map = {} 
        def fibo(n):
            if n == 0:
                return 0
            if n == 1:
                return 1
            if n in map:
                return map[n]
            map[n] = fibo(n-1) + fibo(n-2)
            return map[n]
        return fibo(n)