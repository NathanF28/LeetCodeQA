class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        self.cap = n
        pos = 0
        array = []
        for i in range(1,n+1):
            array.append(i)
        return self.rotate(array,pos,k) 

    def rotate(self, array,pos,k):
        if len(array) == 1:
            return array[0]
        
        pos = (pos + k - 1) % len(array)
        array.remove(array[pos])
        return self.rotate(array,pos,k)

            
