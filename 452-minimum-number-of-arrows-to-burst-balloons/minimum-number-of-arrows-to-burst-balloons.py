class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points = sorted(points)
        count = 1
        curr = points[0]
        print(points)
        print(curr)
        for row in points[1:]:
            if row[0] <= curr[1]:
                curr[1] = min(row[1], curr[1])
            else:
                count+=1
                curr[1] = row[1]
            curr[0] = max(row[0], curr[0])
        return count
            
            