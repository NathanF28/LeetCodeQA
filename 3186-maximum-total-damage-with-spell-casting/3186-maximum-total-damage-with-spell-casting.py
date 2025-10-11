class Solution:
    def maximumTotalDamage(self, power: List[int]) -> int:
        power.sort()
        map = Counter(power)
        unique = sorted(set(power))
        dp = [0] * len(unique)
        j = 0
        _max = 0
        for i in range(len(unique)):
            while j < i and unique[j] < unique[i] - 2:
                _max = max(dp[j], _max)
                j+=1
            dp[i] = _max + (unique[i] * map[unique[i]])
        return max(dp)
