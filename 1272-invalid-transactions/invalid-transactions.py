from collections import defaultdict
from typing import List

class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        # Parse all transactions
        trans = []
        for t in transactions:
            name, time, amount, city = t.split(",")
            trans.append([name, int(time), int(amount), city, t])
        
        # Step 1: find transactions with amount > 1000
        invalid_set = set()
        for t in trans:
            if t[2] > 1000:
                invalid_set.add(t[4])
        
        # Step 2: group by name
        by_name = defaultdict(list)
        for t in trans:
            by_name[t[0]].append(t)
        
        # Step 3: two-pointer check for different cities within 60 minutes
        for name, values in by_name.items():
            values.sort(key=lambda x: x[1])  # sort by time
            n = len(values)
            left = 0
            for right in range(n):
                # Move left to maintain window <= 60 minutes
                while values[right][1] - values[left][1] > 60:
                    left += 1
                # Check all transactions in the window
                for i in range(left, right):
                    if values[i][3] != values[right][3]:
                        invalid_set.add(values[i][4])
                        invalid_set.add(values[right][4])
        
        # Step 4: preserve original order and duplicates
        result = [t for t in transactions if t in invalid_set]
        return result
