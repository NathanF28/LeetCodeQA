class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        costs = sorted(costs, key = lambda x: (x[0] - x[1]))[::-1]
        sume = 0
        n = len(costs)//2
        print(costs)
        for i in range(n):
            sume+= costs[i][1]
            print(costs[i][1])

            sume+= costs[i+n][0]
        return sume