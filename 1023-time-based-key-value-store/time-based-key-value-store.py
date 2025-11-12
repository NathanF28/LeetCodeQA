class TimeMap:

    def __init__(self):
        self.tmap = defaultdict(list)
        self.vmap = defaultdict(str)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.tmap[key].append(timestamp)
        self.vmap[(key, timestamp)] = value
        

    def get(self, key: str, timestamp: int) -> str:
        values = self.tmap[key]
        val = bisect_right(values, timestamp)
        val -= 1
        # print(values, timestamp, val)
        # print(self.vmap)
        # if val == len(values):
        #     val -= 1
        # elif (key, self.tmap[key][val]) not in self.vmap:
        #     val -= 1 

        if not values or timestamp < values[0]:
            return ""

        # print(self.tmap)
        # print(self.vmap)
        # print(self.tmap[key][val])
        return self.vmap[(key, self.tmap[key][val])]
