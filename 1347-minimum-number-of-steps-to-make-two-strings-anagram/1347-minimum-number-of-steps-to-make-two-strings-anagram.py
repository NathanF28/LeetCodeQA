class Solution:
    def minSteps(self, s: str, t: str) -> int:
        map1 = Counter(s)
        map2 = Counter(t)

        return sum((map1 - map2).values())