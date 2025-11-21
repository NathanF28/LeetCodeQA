class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        n = len(s)
        if n < 3:
            return 0

        suf = [0] * n
        mask = 0

        for i in range(n - 1, -1, -1):
            mask |= 1 << (ord(s[i]) - ord('a'))
            suf[i] = mask

        used = [[False] * 26 for _ in range(26)]
        leftMask = 0

        for j in range(1, n - 1):
            leftMask |= 1 << (ord(s[j - 1]) - ord('a'))
            both = leftMask & suf[j + 1]
            mid = ord(s[j]) - ord('a')

            for c in range(26):
                if both & (1 << c):
                    used[c][mid] = True

        ans = 0
        for a in range(26):
            for b in range(26):
                if used[a][b]:
                    ans += 1

        return ans