class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort()
        string = ""
        for one,two in zip(strs[0],strs[-1]):
            if one == two:
                string+= one
            else:
                return string
        return string

