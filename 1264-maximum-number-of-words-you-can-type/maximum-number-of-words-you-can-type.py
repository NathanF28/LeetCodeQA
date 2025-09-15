class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        words = text.split()
        count = 0
        for word in words:
            t = True
            for char in brokenLetters:
                if char in word:
                    t = False
                    break
            if t:
                count+=1
        return count
        