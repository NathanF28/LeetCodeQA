class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        graph = defaultdict(list)
        n = len(quiet)
        for u,v in richer:
            graph[v].append(u)
        answer = [-1] * n
        def dfs(i,_min):
            nonlocal answer
            if answer[i] != -1:
                return answer[i]
            if quiet[i] < quiet[_min]:
                _min = i
            val = _min
            for neighbor in graph[i]:
                candidate = dfs(neighbor, _min)
                if quiet[candidate] < quiet[val]:
                    val = candidate
            return val
        res = []
        for i in range(n):
            x = dfs(i,i)
            answer[i] = x
            res.append(x)
        return res

        