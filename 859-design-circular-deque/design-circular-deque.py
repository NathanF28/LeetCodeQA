class MyCircularDeque:

    def __init__(self, k: int):
        self.q = deque()
        self.cap = k
        

    def insertFront(self, value: int) -> bool:
        if len(self.q) == self.cap:
            return False
        else:
            self.q.appendleft(value)
            return True
        

    def insertLast(self, value: int) -> bool:
        if len(self.q) == self.cap:
            return False
        else:
            self.q.append(value)
            return True

    def deleteFront(self) -> bool:
        if len(self.q) == 0:
            return False
        else:
            self.q.popleft()
            return True

    def deleteLast(self) -> bool:
        if len(self.q) == 0:
            return False
        else:
            self.q.pop()
            return True
    def getFront(self) -> int:
        if len(self.q) == 0:
            return  -1 
        else:
            return self.q[0]
        

    def getRear(self) -> int:
        if len(self.q) == 0:
            return  -1 
        else:
            return self.q[-1]
        

    def isEmpty(self) -> bool:
        return len(self.q) == 0
        

    def isFull(self) -> bool:
        return len(self.q) == self.cap


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()