from collections import defaultdict
from typing import List

class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        trans = []
        for t in transactions:
            name,time,amount,place = t.split(",")
            trans.append([name,int(time),int(amount), place,t])
        
        # Step 1: identify invalid transactions using a set
        invalid_set = set()
        
        # Check amount > 1000
        for t in trans:
            if t[2] > 1000:
                invalid_set.add(t[4])
        
        # Group by name
        by_name = defaultdict(list)
        for t in trans:
            by_name[t[0]].append(t)
        
        # Check different city within 60 minutes
        for name, values in by_name.items():
            values.sort(key=lambda x: x[1])
            n = len(values)
            for i in range(n):
                for j in range(i+1, n):
                    if values[j][1] - values[i][1] > 60:
                        break
                    if values[i][3] != values[j][3]:
                        invalid_set.add(values[i][4])
                        invalid_set.add(values[j][4])
        
        # Step 2: preserve original input order and duplicates
        result = []
        for t in transactions:
            if t in invalid_set:
                result.append(t)
        
        return result
