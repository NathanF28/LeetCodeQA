class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        start = intervals[0][0]
        end = intervals[0][1]
        liste = []
        for initial,final in intervals:
            if initial <= end:
                end = max(end,final)
            else:
                liste.append([start,end])
                start = initial
                end = final
        liste.append([start,end])
        return liste

