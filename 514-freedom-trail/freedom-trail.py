class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        cache = {}
        def rotate(curr,index):
            if (curr,index) in cache:
                return cache[(curr,index)]
            if index == len(key):
                return 0
            res = float('inf') 
            for i in range(len(ring)):
                if ring[i] == key[index]:
                    direction = min(abs(i-curr),abs(len(ring) - abs(i-curr)))
                    res = min(res,direction+1 + rotate(i,index+1) )
            cache[(curr,index)] = res
            return res
            

        
        return rotate(0,0)