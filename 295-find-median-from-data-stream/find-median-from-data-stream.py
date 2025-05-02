class MedianFinder:

    def __init__(self):
        self.liste = []
        

    def addNum(self, num: int) -> None:
        bisect.insort(self.liste,num)
    def findMedian(self) -> float:
        n = len(self.liste)
        if n % 2:
            return float(self.liste[n//2])
        else:
            return float((self.liste[n//2] + self.liste[(n//2) - 1])/2)
            


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()