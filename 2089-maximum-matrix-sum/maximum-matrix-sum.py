class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        cnt = 0
        _min = 2 ** 31
        ans = 0
        for i in range(len(matrix)):
            for j in range(len(matrix)):

                e = matrix[i][j]

                if(e < 0):
                    cnt += 1

                e = abs(e)
                
                if(e < _min):
                    _min = e
                
                ans += e
        
        if(cnt % 2 != 0):
            ans -= _min * 2
        
        return ans