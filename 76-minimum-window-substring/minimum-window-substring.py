class Solution:
    def minWindow(self, s: str, t: str) -> str:
        tmap = Counter(t)
        smap = Counter()
        shortest = ""
        f = float('inf')
        l = 0
        for r in range(len(s)):
            smap[s[r]]+=1
            while l < len(s) and smap[s[l]] > tmap[s[l]]:
                smap[s[l]] -=1
                l+=1
            if tmap <= smap:
                if len(s[l:r+1]) < f:
                    shortest = s[l:r+1]
                    f = len(shortest)
        return shortest
