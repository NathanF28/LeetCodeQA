class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        _max = 0
        l = 0
        check = set()
        for r in range(len(s)):
            while s[r] in check:
                check.remove(s[l])
                l+=1
            check.add(s[r])
            _max = max(r-l+1,_max)
        return _max
            
