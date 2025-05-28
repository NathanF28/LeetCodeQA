class Solution:
    def maxTargetNodes(self, edges1: List[List[int]], edges2: List[List[int]], k: int) -> List[int]:
        tree1= defaultdict(list)
        tree2= defaultdict(list)
        for u,v in edges1:
            tree1[u].append(v)
            tree1[v].append(u)
        for u,v in edges2:
            tree2[u].append(v)
            tree2[v].append(u)
        def bfs(levels,number,which,limit,element_num):
            if limit == 0:
                return element_num
            nonlocal visited
            next = []
            tree = tree1 if which else tree2
            for level in levels:
                for neighbor in tree[level]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        next.append(neighbor)
            element_num+= len(next)
            if len(next) and limit-1 > number:
                element_num = bfs(next,number+1,which,limit,element_num)
            return element_num
        arr = []
        _max_to_connect = 0
        if k > 0:
            for j in range(len(tree2)):
                visited = set()
                visited.add(j)
                check = bfs([j],0,0,k-1,1)
                _max_to_connect = max(_max_to_connect,check)
        for i in range(len(tree1)):
            visited = set()
            visited.add(i)
            initial = bfs([i],0,1,k,1)
            arr.append(initial + _max_to_connect)
        return arr




