class UndergroundSystem:

    def __init__(self):
        self.map = {}
        self.tup = defaultdict(list)
        

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.map[id] = [stationName,t]
        

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        A, startTime = self.map[id]
        self.tup[(A, stationName)].append(t-startTime)
        

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        return sum(self.tup[(startStation,endStation)]) / len(self.tup[(startStation, endStation)])
        


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)