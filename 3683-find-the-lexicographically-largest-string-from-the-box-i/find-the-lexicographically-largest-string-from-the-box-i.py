class Solution:
    def answerString(self, s: str, n: int) -> str:
        return n>1 and max(s[i:i+len(s)-n+1] for i in range(len(s))) or s