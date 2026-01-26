class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arre = sorted(arr)
        mine = float('inf')
        for i in range(1, len(arre)):
            res = arre[i] - arre[i-1]
            mine = min(mine,res)
        print(mine)    
        ans = []    
        for j in range(1,len(arre)):
            if arre[j] - arre[j-1] == mine:
                ans.append([arre[j-1],arre[j]])
        return ans            





         