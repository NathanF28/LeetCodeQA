class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:
        parent = defaultdict(str)
        def equalizer(s1,s2):
            l = 0
            n = len(s1)
            count = 0
            if len(s1) != len(s2):
                return False
            for i in range(n):
                if s1[i] != s2[i]:
                    count+=1
            return count == 2
        def find(string):
            if string not in parent:
                parent[string] = string
            if string != parent[string]:
                parent[string] = find(parent[string])
            return parent[string]
        def union(x,y):
            parx,pary = find(x),find(y)
            if equalizer(x,y):
                parent[pary] = parx 
        for i in range(len(strs)):
            for j in range(len(strs)):
                union(strs[i],strs[j])
        for string in strs:
            find(string)
        return len(set(parent.values()))

                    
