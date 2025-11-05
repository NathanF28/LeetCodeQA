class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []
        for stone in stones:
            heappush(heap,-stone)
        
        while len(heap) > 1:
            first = -heappop(heap)
            second = -heappop(heap)
            if first == second:
                continue
            heappush(heap,-(first-second))
        return -heap[0] if heap else 0 