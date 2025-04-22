class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        
        directions = [(0,1),(1,0),(-1,0),(0,-1)]
        def inbound(row,col):
            return 0 <= row < len(image) and 0 <= col < len(image[0])
        og = image[sr][sc]
        visited = [ [False for _ in range(len(image[0]))] for _ in range(len(image)) ]
        def dfs(row,col):
            if image[row][col] != og:
                return
            visited[row][col] = True
            image[row][col] = color
            for direction in directions:
                new_row = direction[0] + row
                new_col= direction[1] + col
                if inbound(new_row,new_col) and not visited[new_row][new_col]:
                    dfs(new_row,new_col)
        dfs(sr,sc)
        return image

        