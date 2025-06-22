class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:

        final = []
        i = 0
        while i < len(s):
            j = i + k 
            string = ""
            while i < j:
                if i < len(s):
                    string+= s[i]
                else:
                    string+= fill
                i+=1
            final.append(string)
        return final 