class Solution:
    def numSub(self, s: str) -> int:
        
        count = 0 
        curr = 0
        for char in s:
            if char == '1':
                curr+=1
            else:
                count += (curr * (curr+1))//2
                curr = 0
        count += (curr * (curr+1))//2
        return count % (10 **9 + 7)

