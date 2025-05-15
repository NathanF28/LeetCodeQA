class Solution:
    def wonderfulSubstrings(self, word: str) -> int:
        pref = defaultdict(int)
        pref[0] = 1
        mask = 0
        res = 0
        for char in word:
            mask ^=  1 << (ord(char) - 97)
            res += pref[mask]

            for i in range(10):
                check = mask ^ ( 1 << i)
                res+=pref[check]
            pref[mask]+=1
        return res