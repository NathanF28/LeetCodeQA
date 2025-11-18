class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        res = ""
        if len(str1) > len(str2):
            word = str2
        else:
            word = str1

        for i in range(len(word)+1):
            if str1.count(word[:i+1]) * (i+1) == len(str1) and str2.count(word[:i+1]) * (i+1) == len(str2):
                res = word[:i+1]
        
        return res 

                