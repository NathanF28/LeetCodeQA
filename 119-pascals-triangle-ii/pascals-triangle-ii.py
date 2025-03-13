class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        prev = self.getRow(rowIndex-1)
        next = [1] * (len(prev) + 1)
        for i in range(1,len(next)-1):
            next[i] = prev[i] + prev[i-1]
        return next

        
        