class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        seen = set()
        map = {}
        for i in range(len(s)-9):
            sub = s[i:i+10]
            if sub not in map:
                map[sub] = 1
            else:
                seen.add(sub)
        return list(seen)       

        