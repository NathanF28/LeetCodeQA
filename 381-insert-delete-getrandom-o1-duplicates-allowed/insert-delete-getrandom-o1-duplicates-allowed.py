class RandomizedCollection:

    def __init__(self):
        self.list = []
        self.map = {}
        

    def insert(self, val: int) -> bool:

        self.list.append(val)

        if val in self.map:
            self.map[val].add(len(self.list)-1) 
            return False

        self.map[val] = {len(self.list)-1}

        return True
        
        

    def remove(self, val: int) -> bool:
        if val not in self.map:
            return False
        
        index = self.map[val].pop()

        last_num = self.list[-1]

        self.list[index] = last_num
        self.map[last_num].discard(len(self.list)-1)
        if len(self.list)-1 != index:
            self.map[last_num].add(index)

        self.list.pop()
        if len(self.map[val]) == 0:
            del self.map[val] 
        return True 

    def getRandom(self) -> int:
        return random.choice(self.list) 


# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()