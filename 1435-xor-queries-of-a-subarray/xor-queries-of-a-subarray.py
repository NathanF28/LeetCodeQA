class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        for i in range(1,len(arr)):
            arr[i] ^= arr[i-1]
        f = []
        for l,r in queries:
            if not l:
                f.append(arr[r])
            else:
                f.append(arr[l-1] ^ arr[r])
        return f