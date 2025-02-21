class Solution:
    def reverse(self, x: int) -> int:
        count = 0
        if x < 0:
            count = 1
            x = -x
        x = str(x)
        x = x[::-1]
        if int(x) >  2147483648 or int(x) < -2147483648:
            return 0
        if count == 1:
            return -int(x)
        return int(x)    
        