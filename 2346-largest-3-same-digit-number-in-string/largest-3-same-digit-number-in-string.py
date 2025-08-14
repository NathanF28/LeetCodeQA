class Solution:
    def largestGoodInteger(self, num: str) -> str:
        dig = ""
        _max = 0
        for i in range(len(num)-2):
            string = num[i:i+3]
            if len(set(string)) == 1:
                n = int(string)
                if n >= _max:
                    dig = string
                    _max = n
        return dig 


