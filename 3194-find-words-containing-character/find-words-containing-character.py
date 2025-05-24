class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        final = []
        for i in range(len(words)):
            if x in words[i]:
                final.append(i)
        return final
        