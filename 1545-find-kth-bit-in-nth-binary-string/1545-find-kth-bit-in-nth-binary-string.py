class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        def reverseinvert(string: str):
            string = list(string)
            for i in range(len(string)):
                if string[i] == "1":
                    string[i] = "0" 
                else:
                    string[i] = "1"
            return "".join(string)[::-1]
        
        def findtheNum(n):
            if n == 1:
                return "0"
            return findtheNum(n-1) + "1" + reverseinvert(findtheNum(n-1))
        
        return findtheNum(n)[k-1]
        