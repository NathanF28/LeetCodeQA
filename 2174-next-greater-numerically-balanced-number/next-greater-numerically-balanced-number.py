class Solution:
    def nextBeautifulNumber(self, n: int) -> int:
        for i in range(n+1,10**18):
            possible = True
            map = Counter(str(i))
            for char in str(i):
                if map[char] != int(char):
                    possible = False
                    break
            if possible:
                return i