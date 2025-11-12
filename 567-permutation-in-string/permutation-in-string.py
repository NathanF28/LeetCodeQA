class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        window = len(s1)

        st = Counter(s1)

        for r in range(len(s2)):
            pap = Counter(s2[r:window+r])
            if pap == st:
                return True
        return False
