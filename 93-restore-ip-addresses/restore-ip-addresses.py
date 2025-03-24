class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        possible = []
        map = {}
        n = len(s)
        def backtrack(string,path):  
            if len(path) > 0 and len(path[-1]) > 1 and path[-1][0] == "0" or len(path) > 0 and  int(path[-1]) > 255:
                return
            if len(path) == 4:
                if string == "":
                    tup = tuple(path[:])
                    if tup not in map:
                        liste = ".".join(path[:])
                        possible.append(liste)
                        map[tup] = 1
                return
            if len(string) < 4 - len(path):
                return
            for i in range(3):
                slic = string[:i+1]
                path.append(slic)
                remaining = string[i+1:]
                backtrack(remaining,path)
                path.pop()
        backtrack(s,[])
        return possible