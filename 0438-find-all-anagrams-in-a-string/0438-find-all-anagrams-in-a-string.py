class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        liste = []
        n = len(p)
        p = sorted(p)
        for i in range(len(s)-n+1):
            sub = sorted(s[i:i+n])
            if p == sub:
                liste.append(i)
        return liste        
        