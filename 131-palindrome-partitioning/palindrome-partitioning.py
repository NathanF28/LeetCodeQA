class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        possible = []

        def split(path, string):
            if len(string) == 0:
                possible.append(path[:])
                return 
            for i in range(len(string)):
                substring = string[:i+1]
                if substring == substring[::-1]:
                    path.append(substring)
                    split(path,string[i+1:])
                    path.pop()
        split([], s)
        return possible
