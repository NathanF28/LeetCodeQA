class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        red = defaultdict(list)
        blue = defaultdict(list)
        ans = [-1] * n
        for src,dest in redEdges:
            red[src].append(dest)
        for src,dest in blueEdges:
            blue[src].append(dest)
        q = deque()
        visit = set()
        q.append((0,0,"None"))

        while q:
            node,length,color = q.popleft()
            if ans[node] == -1:
                ans[node] = length
            
            if color != "RED":
                for nei in red[node]:
                    if (nei,"RED") not in visit:
                        visit.add((nei,"RED"))
                        q.append((nei,length+1,"RED"))

            if color != "BLUE":
                for nei in blue[node]:
                    if (nei,"BLUE") not in visit:
                        visit.add((nei,"BLUE"))
                        q.append((nei,length+1,"BLUE"))
        return ans
