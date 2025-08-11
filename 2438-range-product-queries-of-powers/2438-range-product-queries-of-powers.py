class Solution:
    def productQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        MOD = 10 ** 9 + 7
        val = str(bin(n))
        n = len(val)
        arr = []
        for i in range(len(val)-1, 1, -1):
            if val[i] != "0":
                arr.append(2**(n-i-1))
        for i in range(1,len(arr)):
            arr[i]*=arr[i-1]
        arr.append(1)
        final = []
        for a,b in queries:
            ans = arr[b]//arr[a-1]
            final.append(ans % MOD)
        return final
            