class OrderedStream:

    def __init__(self, n: int):
        self.ptr = 1
        self.stream = [None] * (n+1)
        

    def insert(self, idKey: int, value: str) -> List[str]:
        self.stream[idKey]= value
        liste = []
        for i in range(self.ptr, len(self.stream)):
            if self.stream[i]:
                liste.append(self.stream[i])
            else:
                self.ptr = i
                break
        return liste
        


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)