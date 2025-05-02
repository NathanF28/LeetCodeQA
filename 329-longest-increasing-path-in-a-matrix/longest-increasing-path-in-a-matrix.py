class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:

        directions  = [(0,1),(1,0),(-1,0),(0,-1)]
        def inbound(row,col):
            return 0 <= row < len(matrix) and 0 <= col < len(matrix[0])

        graph = defaultdict(list)
        indeg = defaultdict(int)
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                for dr,dc in directions:
                    nr = i+dr
                    nc = j+dc
                    if inbound(nr,nc) and matrix[nr][nc] > matrix[i][j]:
                        graph[(i,j)].append((nr,nc))
                        indeg[(nr,nc)]+=1
        q = deque()
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                    if indeg[(i,j)] == 0:
                        q.append((i,j))
                        print("For",(i,j))
                        print(graph[(i,j)])
        length = 0
        while q:
            for i in range(len(q)):
                node = q.popleft()
                for nr,nc in graph[node]:
                    indeg[(nr,nc)]-=1
                    if indeg[(nr,nc)] == 0:
                        q.append((nr,nc))
            length+=1
        return length 