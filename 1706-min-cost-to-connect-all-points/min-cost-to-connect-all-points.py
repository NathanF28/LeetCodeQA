class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        def euclid(p1,p2):
            x1,y1 = p1
            x2,y2 = p2
            return abs(x2-x1) + abs(y2-y1)
        edges = len(points) - 1
        heap = []
        for i in range(edges+1):
            for j in range(i+1,edges+1):
                p1 = points[i]
                p2 = points[j]
                weight = euclid(p1,p2)
                heappush(heap,[weight,p1,p2])
        total = 0
        parent = {}
        rank = defaultdict(lambda: 1)
        def find(tup):
            if tup not in parent:
                parent[tup] = tup
                return tup
            if parent[tup] != tup:
                parent[tup] = find(parent[tup])
            return parent[tup]
        def union(tup1,tup2):
            parx,pary = find(tup1),find(tup2)

            if parx == pary:
                return True

            if rank[parx] > rank[pary]:
                parent[pary] = parx

            elif rank[parx] < rank[pary]:
                parent[parx] = pary
            else:
                parent[pary] = parx
                rank[parx]+=1

            return False


        while edges:
            weight,p1,p2 = heappop(heap)
            p1  = tuple(p1)
            p2 = tuple(p2)
            if not union(p1,p2):
                edges-=1
                total+=weight
        return total

