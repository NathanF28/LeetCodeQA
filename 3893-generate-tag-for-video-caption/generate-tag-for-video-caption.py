class Solution:
    def generateTag(self, caption: str) -> str:
        s = caption.title().split()
        if not s:
            return "#"
        res = "#" + s[0].lower() + "".join(s[1:])
        return res[:100]
