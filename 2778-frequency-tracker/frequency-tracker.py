class FrequencyTracker:

    def __init__(self):
        self.hashmap = defaultdict(int)
        self.valuemap = defaultdict(int)

    def add(self, number: int) -> None:
        prevfreq = self.hashmap[number]
        currfreq = prevfreq + 1

        self.hashmap[number] = currfreq

        # decrease prev value from value map
        if prevfreq > 0:
            self.valuemap[prevfreq] -=1

        # update new value to value map
        self.valuemap[currfreq] +=1

    def deleteOne(self, number: int) -> None:
        prevfreq = self.hashmap[number]

        if prevfreq != 0:
            currfreq = prevfreq - 1
            self.hashmap[number] = currfreq

            self.valuemap[prevfreq]-=1

            if currfreq > 0:
                self.valuemap[currfreq] +=1 


    def hasFrequency(self, frequency: int) -> bool:
        return self.valuemap[frequency] > 0 


# Your FrequencyTracker object will be instantiated and called as such:
# obj = FrequencyTracker()
# obj.add(number)
# obj.deleteOne(number)
# param_3 = obj.hasFrequency(frequency)