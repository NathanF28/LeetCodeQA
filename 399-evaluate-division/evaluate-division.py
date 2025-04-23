class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(list)
        map = {}
        for i in range(len(equations)):
            first = equations[i][0]
            second = equations[i][1]
            map[(first,second)] = values[i]
            map[(second,first)] = 1  / values[i]
            graph[first].append(second)
            graph[second].append(first)
        final = defaultdict(int)
        def istherePath(source,destination,visited,answer,_sum):
            nonlocal graph
            nonlocal map
            if source not in graph or destination not in graph:
                return answer
            if source == destination:
                answer = _sum
                return answer
            visited[source] = 1
            for neighbor in graph[source]:
                if not visited[neighbor]:
                    _sum *= map[(source,neighbor)]
                    answer = istherePath(neighbor,destination,visited,answer,_sum)
                    _sum /= map[(source,neighbor)]
            return answer
        final = [] 
        for query in queries:
            visited = defaultdict(int)
            source = query[0] 
            destination = query[1]
            final.append(istherePath(source,destination,visited,-1.00000,1))
        return final