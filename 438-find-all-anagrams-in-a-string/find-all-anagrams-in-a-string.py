class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:

        standard = Counter(p)
        window_size = len(p)
        rolling = Counter()
        if len(p) > len(s):
            return []
        for i in range(window_size):
            rolling[s[i]]+=1
        count = 0 
        res = []
        if rolling == standard:
            res.append(0)
        left = 0 
        for right in range(window_size,len(s)):
            rolling[s[right]]+=1
            rolling[s[left]]-=1
            if rolling[s[left]] == 0:
                del rolling[s[left]]
            if rolling == standard:
                res.append(left+1)
            left+=1
        return res
        


