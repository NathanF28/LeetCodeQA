class Spreadsheet:

    def __init__(self, rows: int):
        self.hashmap = defaultdict(int)
        

    def setCell(self, cell: str, value: int) -> None:
        self.hashmap[cell] = value
        
    def resetCell(self, cell: str) -> None:
        self.hashmap[cell] = 0    

    def getValue(self, formula: str) -> int:
        for i in range(len(formula)):
            if formula[i]== "+":
                left = formula[1:i]
                right = formula[i+1:]
                break
        if not left.isdigit():
            left = self.hashmap[left]
        if not right.isdigit():
            right = self.hashmap[right]
        return int(left) + int(right)
        


        


# Your Spreadsheet object will be instantiated and called as such:
# obj = Spreadsheet(rows)
# obj.setCell(cell,value)
# obj.resetCell(cell)
# param_3 = obj.getValue(formula)