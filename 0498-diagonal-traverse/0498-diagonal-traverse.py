class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        map = {}
        rows = len(mat)
        col = len(mat[0])
        for i in range(rows):
            for j in range(col):
                if i+j not in map:
                    map[i+j] = [mat[i][j]]
                else:
                    map[i+j].append(mat[i][j])
        liste = []
        for key,value in map.items():
            if key % 2 == 0:
                liste.append(value[::-1])
            else:
                liste.append(value)
        ans = []
        for row in liste:
            for j in row:
                ans.append(j)
        return ans
        