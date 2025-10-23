class Solution:
    def hasSameDigits(self, s: str) -> bool:
        

        def cut(string):
            if len(string) == 2:
                return string

            new = ""
            for i in range(len(string)-1):
                a = int(string[i])
                b = int(string[i+1])
                new+= str((a+b)%10)
            return cut(new)
        string = cut(s)
        return string[0] == string[-1]