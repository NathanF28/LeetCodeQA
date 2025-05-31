class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        graph = defaultdict(list)
        for i in range(len(edges)):
            if edges[i] != -1:
                graph[i].append(edges[i])
        dist1 = defaultdict(lambda : float('inf'))
        dist2 = defaultdict(lambda : float('inf'))
        index = -1
        dis = float('inf')
        visited = set()
        def dfs(node,which,level):
            dist = dist1 if which == 1 else dist2
            dist[node] = level
            visited.add(node)
            for neighbor in graph[node]:
                if neighbor not in visited:
                    dfs(neighbor,which,level+1)
        dfs(node1,1,0)
        visited = set()
        dfs(node2,0,0)
        for i in range(len(edges)):
            val = max(dist1[i], dist2[i])
            if val == dis:
                if i < index:
                    index = i
            elif val < dis:
                dis = val
                index = i
        return index



        