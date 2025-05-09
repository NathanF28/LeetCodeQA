class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:

        parent = defaultdict(str)

        def find(letter):
            if letter not in parent:
                parent[letter] = letter
            if letter != parent[letter]:
                parent[letter] = find(parent[letter])
            return parent[letter]
        def union(x,y):
            parx,pary = find(x),find(y)
            if parx == pary:
                return 

            if ord(parx) < ord(pary):
                parent[pary]  = parx
            else:
                parent[parx]  = pary

        for i in range(len(s1)):
            union(s1[i],s2[i])
        string = ""
        for char in baseStr:
            find(char)
            string+=parent[char]
        return string


        