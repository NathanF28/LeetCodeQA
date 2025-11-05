class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        def dist(x,y):
            return -((x**2) + (y**2))** 0.5
        

        heap = []
        for x,y in points:
            p = [dist(x,y), [x,y]]
            heappush(heap,p)
        while len(heap) > k:
            heappop(heap)
        ans = []
        for point in heap:
            ans.append(point[1])
        return ans

        