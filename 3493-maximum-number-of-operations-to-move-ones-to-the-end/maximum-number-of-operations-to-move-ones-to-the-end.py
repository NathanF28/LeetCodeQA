class Solution:
    def maxOperations(self, s: str) -> int:

        counted_ones = 0
        operations = 0
        
        for i,ch in enumerate(s):

            if ch =="1":
                counted_ones +=1

            else:
                if i ==0 or s[i-1] =="1":
                    operations += counted_ones
        
        return operations