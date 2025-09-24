class Solution:
    def generateTag(self, caption: str) -> str:
        s = caption.title().split()
        if not s:
            return "#"
        return "".join("#" + s[0].lower() + "".join(s[1:]))[:100] 
