class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        parent = {}
        def find(tup):
            if tup not in parent:
                parent[tup] = tup
                return tup
            if tup != parent[tup]:
                parent[tup] = find(parent[tup])
            return parent[tup]

        def union(x,y):
            parx,pary, = find(x),find(y)
            parent[pary] = parx

        for i in range(len(stones)):
            x1,y1  = stones[i]
            for j in range(i+1,len(stones)):
                x2,y2 = stones[j]
                if x1 == x2 or y1 == y2:
                    union(i,j)
        for i in range(len(stones)):
            find(i)
        val = len(set(parent.values()))
        return len(stones) - val
                



        