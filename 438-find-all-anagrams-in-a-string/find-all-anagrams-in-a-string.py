class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        k = len(p)
        if k > len(s):
            return []
        res = []
        window = Counter()
        map = Counter(p)
        for i in range(k):
            window[s[i]]+=1
        
        if window ==  map:
            res.append(0)
        left = 0
        for i in range(k, len(s)):
            window[s[i]]+=1
            window[s[left]]-=1
            if window[s[left]] == 0:
                del window[s[left]] 

            if window == map:
                res.append(left+1)
            left+=1
        return res

