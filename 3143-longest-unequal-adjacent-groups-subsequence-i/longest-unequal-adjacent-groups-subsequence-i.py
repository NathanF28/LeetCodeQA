class Solution:
    def getLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        ans = [0]
        for i in range(1,len(groups)):
            if groups[i] != groups[ans[-1]]:
                ans.append(i)
        print(ans)
        final = []
        for index in ans:
            final.append(words[index])
        return final