class Solution:
    def numSub(self, s: str) -> int:

        total = 0
        curr = 0
        for b in s:
            if b == "1":
                curr+=1
            else:
                total+= (curr * (curr+1) // 2)
                curr = 0
        total+= (curr * (curr+1) // 2)
        return total % (10**9 + 7)


        