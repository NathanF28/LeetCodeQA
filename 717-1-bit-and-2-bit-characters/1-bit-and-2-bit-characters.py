class Solution:
    def isOneBitCharacter(self, bits: list[int]) -> bool:
        bits.pop()
        n = len(bits)

        if n == 0 or bits[-1] == 0:
            return True

        i = 0
        while i < n - 1:
            i += bits[i] + 1

        return i == n