class Solution:
    def convert(self, s: str, numRows: int) -> str:
        rows = [[] for _ in range(numRows)]
        count = 0
        dir = -1
        if numRows == 1:
            return s
        for char in s:
            if count == numRows:
                dir = 1
            if count == 1:
                dir = -1
            if dir == -1:
                count+=1
            else:
                count-=1
            rows[count-1].append(char)
        string = ""
        for row in rows:
            string+= "".join(row)
        return string

        