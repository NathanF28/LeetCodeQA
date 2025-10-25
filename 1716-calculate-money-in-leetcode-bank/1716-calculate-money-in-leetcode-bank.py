class Solution:
    def totalMoney(self, n: int) -> int:
        map = defaultdict(int)
        for i in range(1,n+1):
            map[i%7]+=1
        _sum = 0
        map[7] = map[0]
        for i in range(1,8):
            for j in range(i,i+map[i]):
                _sum += j
        return _sum