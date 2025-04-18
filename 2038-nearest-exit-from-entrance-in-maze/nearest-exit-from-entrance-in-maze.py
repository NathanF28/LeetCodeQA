class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        directions = [(0,1),(1,0),(-1,0),(0,-1)] 
        visited = [[False for _ in range(len(maze[0]))] for _ in range(len(maze))]
        def inbound(row,col):
            return 0 <= row < len(maze) and 0 <= col < len(maze[0])
        def edgebound(row,col):
            if row == 0 or row == len(maze)-1:
                return True
            if col == 0 or col == len(maze[0])-1:
                return True
            return False
        furthest = float('inf')
        def bfs(path,level):
            nonlocal furthest
            if len(path) == 0:
                return 
            next = []
            for liste in path: 
                print(liste)
                if edgebound(liste[0],liste[1]) and maze[liste[0]][liste[1]] == "." and liste != entrance: 
                    furthest = min(level,furthest)
                for direction in directions:
                    new_row = liste[0] + direction[0]
                    new_col= liste[1] +direction[1]
                    if inbound(new_row,new_col) and not visited[new_row][new_col] and  maze[new_row][new_col] == "." :
                        next.append([new_row,new_col])
                        visited[new_row][new_col] = True
            bfs(next,level+1)
        bfs([entrance],0)
        return furthest if furthest != float('inf') else -1
