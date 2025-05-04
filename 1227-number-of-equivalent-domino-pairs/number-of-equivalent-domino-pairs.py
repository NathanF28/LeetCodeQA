class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        map = defaultdict(int)
        for dom in dominoes:
            tup = tuple(sorted(dom))
            map[tup] +=1
        count= 0
        for key,value in map.items():
            if value > 1:
                x = value-1
                count+= (x * (x+1)) // 2

        return count 