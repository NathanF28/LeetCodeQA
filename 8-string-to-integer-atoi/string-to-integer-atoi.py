class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.lstrip()
        if len(s) == 0:
            return 0
        neg = s[0] == "-"
        start = 0 if s[0] != "+" and not neg else 1
        string = ""
        for char in s[start:]:
            if char.isdigit():
                string+=char
            else:
                break
        if len(string) == 0:
            return 0
        
        num = int(string)
        num = -1* num if neg else num
        INT_MIN, INT_MAX = -2**31, 2**31 - 1
        if num < INT_MIN:
            return INT_MIN
        if num > INT_MAX:
            return INT_MAX
        return num
        

            
        