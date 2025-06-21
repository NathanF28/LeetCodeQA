class Solution:
    def minimumDeletions(self, word: str, k: int) -> int:
        map = Counter(word)
        liste = set(word)
        _min = float('inf')
        for char in liste:
            res = 0
            st = map[char]
            for key,value in map.items():
                if key == char:
                    continue
                if value < st:
                    res += value
                elif value > st + k:
                    res += value - (st+k)
            _min = min(res,_min)
        return _min
