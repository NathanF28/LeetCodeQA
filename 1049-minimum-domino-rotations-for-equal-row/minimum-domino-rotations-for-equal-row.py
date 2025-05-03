class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        
        def check(num):
            rotate_top = 0
            rotate_bottom = 0
            for i in range(len(tops)):
                if num != tops[i] and num != bottoms[i]:
                    return float('inf')
                if num != tops[i]:
                    rotate_top +=1
                if num != bottoms[i]:
                    rotate_bottom+=1
            return min(rotate_top,rotate_bottom)
        
        ans = min(check(tops[0]),check(bottoms[0])) 
        return ans if ans != float('inf') else -1