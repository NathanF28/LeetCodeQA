class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        binl = bin(left)[2:].zfill(32)
        binr = bin(right)[2:].zfill(32)
        pref = ""
        for i1,i2 in zip(binl,binr):
            if i1 == i2:
                pref+= i1
            else:
                break
        pref += '0' * (32 - len(pref))
        return int(pref,2)
