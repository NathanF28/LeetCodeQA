class TaskManager:

    def __init__(self, tasks: List[List[int]]):
        self.taskHeap = []  # determine execution order (max-heap)
        self.taskMap = {}
        for u,t,p in tasks:
            heappush(self.taskHeap, (-p, -t, u))
            self.taskMap[t] = [p,u]




    def add(self, userId: int, taskId: int, priority: int) -> None:
        heappush(self.taskHeap, (-priority, -taskId, userId))
        self.taskMap[taskId] = [priority,userId]
        

    def edit(self, taskId: int, newPriority: int) -> None:
        _, userId = self.taskMap[taskId]
        self.taskMap[taskId] = [newPriority,userId]
        heappush(self.taskHeap, (-newPriority, -taskId, userId))

    def rmv(self, taskId: int) -> None:
        del self.taskMap[taskId]

    def execTop(self) -> int:
        while self.taskHeap:
            priority, taskId, userId = heappop(self.taskHeap)
            if -taskId not in self.taskMap:
                continue
            oldPriority, oldUserId = self.taskMap[-taskId]
            if -priority != oldPriority or -taskId not in self.taskMap or userId != oldUserId:
                continue
            del self.taskMap[-taskId]
            return userId
        return -1


# Your TaskManager object will be instantiated and called as such:
# obj = TaskManager(tasks)
# obj.add(userId,taskId,priority)
# obj.edit(taskId,newPriority)
# obj.rmv(taskId)
# param_4 = obj.execTop()