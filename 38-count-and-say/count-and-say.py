class Solution:
    def countAndSay(self, n: int) -> str:

        def compress(string):
            final = ""
            l = 0
            count = 0
            for r in range(len(string)):
                if string[r] != string[l]:
                    final+= str(count)
                    final+= string[l]  
                    count = 0
                    l = r
                count+=1
            final+= str(count)
            final+= string[l]  
            return final
        ans = ""
        def recursion(s, round):
            nonlocal ans
            if round == n:
                ans+=s
                return
            new = compress(s)
            return recursion(new,round+1)
        x = recursion("1",1)
        return ans
            


        
        