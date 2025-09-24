class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        invalid = set()
        by_name = defaultdict(list)
        trans = []

        # filter out > 1000$ and convert time and amount to int
        for t in transactions:
            name,time,amount,place = t.split(",")
            if int(amount) > 1000:
                invalid.add(t)
            trans.append([name,int(time), int(amount), place, t])
        
        # categorize by name 
        for t in trans:
            by_name[t[0]].append(t)

        # Find invalids for by name
        for name, ts in by_name.items():
            #sort them by time 
            ts.sort(key = lambda x : x[1])
            left = 0
            n = len(ts)
            for right in range(n):
                # discard window gaps greater than 60 mins
                while ts[right][1] - ts[left][1] > 60:
                    left+=1
                
                for i in range(left,right):
                    if ts[i][3] != ts[right][3]:
                        invalid.add(ts[i][4])
                        invalid.add(ts[right][4])

        final = []
        for t in transactions:
            if t in invalid:
                final.append(t)
        return final

            

