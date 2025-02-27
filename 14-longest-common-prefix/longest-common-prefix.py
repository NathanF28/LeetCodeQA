class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        letter = ""
        strs.sort()
        for i in range(min(len(strs[0]),len(strs[-1]))):
            if strs[0][i] != strs[-1][i]:
                break
            letter+=strs[0][i]
        return letter
