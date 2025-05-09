class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)
        parent = defaultdict(tuple)
        size = defaultdict(lambda : 1)

        def find(node):
            if node not in parent:
                parent[node] = node
                size[node] = 1
            if node != parent[node]:
                parent[node] = find(parent[node])
            return parent[node] 

        def union(x,y):
            rootx,rooty = find(x),find(y)
            if size[rootx] > size[rooty]:
                parent[rooty] = rootx
                size[rootx]+=size[rooty]
            else:
                parent[rootx] = rooty
                size[rooty]+=size[rootx]
        def inbound(row,col):
            return 0 <= row < n and 0 <= col < n

        visited = [[False for _ in range(n)] for __ in range(n)]    
        directions = [(0,1),(1,0),(-1,0),(0,-1)]

        def dfs(row,col):
            visited[row][col] = True
            for dx,dy in directions:
                nr = row + dx
                nc = col + dy
                if inbound(nr,nc) and not visited[nr][nc] and grid[nr][nc]:
                    union((row,col),(nr,nc))
                    dfs(nr,nc)
        for i in range(n):
            for j in range(n):
                if not visited[i][j] and grid[i][j]:
                    dfs(i,j)
                    find((i,j))
        largest = max(size.values()) if size else 0
        for i in range(n):
            for j in range(n):
                if not grid[i][j]:
                    seen = {}
                    for dx,dy in directions:
                        nr = i + dx
                        nc = j + dy
                        if inbound(nr,nc) and grid[nr][nc]:
                            print(nr,nc)
                            par = find((nr,nc))
                            if par not in seen:
                                seen[par] = size[par]
                    largest = max(largest,sum(seen.values())+1)
        return largest 

        
        
            



        