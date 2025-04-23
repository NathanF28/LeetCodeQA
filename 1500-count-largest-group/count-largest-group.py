class Solution:
    def countLargestGroup(self, n: int) -> int:
        mapp = defaultdict(int)
        for i in range(1,n+1):
            string = list(map(int,str(i)))
            mapp[sum(string)]+=1
        count = defaultdict(int)
        for key,value in mapp.items():
            count[value]+=1
        highest = sorted(count)[-1]
        return count[highest]


        