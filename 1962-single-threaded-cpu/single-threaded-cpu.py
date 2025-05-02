class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        for i in range(len(tasks)):
            tasks[i].append(i)
        tasks.sort(key = lambda t: t[0])
        time = tasks[0][0]
        res = []
        heap = []
        i = 0
        while heap or i < len(tasks):
            while i < len(tasks) and time >= tasks[i][0]:
                heapq.heappush(heap,(tasks[i][1],tasks[i][2]))
                i+=1
            if not heap:
                time = tasks[i][0]
            else:
                burst,index = heapq.heappop(heap)
                time+=burst
                res.append(index)
        return res

            