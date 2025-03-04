class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        for i in range(16,-1,-1):
            val = 3 ** i
            if n >= val:
                n-= val
        return n == 0

        