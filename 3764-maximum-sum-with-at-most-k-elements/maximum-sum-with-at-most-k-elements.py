class Solution:
    def maxSum(self, grid: List[List[int]], limits: List[int], k: int) -> int:
        candidates = []
        for i in range(len(grid)):
            heapq.heapify(grid[i])
            liste = nlargest(limits[i],grid[i])
            candidates.extend(liste)
        heapq.heapify(candidates)
        final = nlargest(k,candidates)
        return sum(final)

        