class Solution:
    def partition(self, s: str) -> List[List[str]]:


        possible = [] 
        def split(string,path):
            if len(string) == 0:
                possible.append(path[:])

            for i in range(len(string)):
                sub = string[:i+1]
                if sub == sub[::-1]:
                    path.append(sub)
                    split(string[i+1:],path)
                    path.pop()
        split(s,[])
        return possible
                