class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        l = 0 
        r = l+1
        count = 0
        while l < len(colors):
            print(l,r)
            j = r % len(colors)
            if colors[j] != colors[j-1]:
                r+=1
            else:
                l = r
                r = l+1
            if r-l == k:
                count+=1
                l+=1
        return count
        