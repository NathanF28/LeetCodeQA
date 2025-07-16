class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        e = 0
        o = 0 
        for num in nums:
            if num & 1:
                o+=1
            else:
                e+=1
        ae = 0
        se = 1
        ao = 0
        so = 1
        for num in nums:
            if num & 1:
                if se == -1:
                    se = 1
                    ae+=1
                if so == 1:
                    so = -1
                    ao+=1
            else:
                if se == 1:
                    se = -1
                    ae+=1
                if so == -1:
                    so = 1
                    ao+=1
        return max(e,o,ao,ae)

            
