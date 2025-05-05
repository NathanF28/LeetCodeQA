class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        parent = [i for i in range(len(accounts))]
        rank = [1] * len(accounts)
        emailmap = defaultdict(int)
        def find(index):
            if parent[index] != index:
                parent[index] = find(parent[index])
            return parent[index]

        def union(x,y):
            parx, pary = find(x), find(y)

            if parx == pary:
                return False
            
            if rank[parx] > rank[pary]:
                parent[pary] = parx
                rank[parx] += rank[pary]
            else:
                parent[parx] = pary
                rank[pary] += rank[parx]

        for i in range(len(accounts)):
            possible_parent = accounts[i][0]
            for email in accounts[i][1:]:
                if email not in emailmap:
                    emailmap[email] = i
                else:
                    union(i,emailmap[email])
        group = defaultdict(list)
        for key,value in emailmap.items():
            rep = find(value)
            group[rep].append(key)
        final = []
        for name, emails in group.items():
            temp = []
            temp.append(accounts[name][0])
            check = sorted(emails)
            temp.extend(check)
            final.append(temp)
        return final

        