class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        map = {}
        for i in range(len(s)):
            map[s[i]] = i
        liste=  []
        print(map)
        position = map[s[0]]
        last = 0
        for i in range(1,len(s)):
            if i > position:
                liste.append(i-last)
                last = i
            position = max(position,map[s[i]])
        liste.append(len(s)-last)
        return liste