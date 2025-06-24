class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        ind = []
        for i in range(len(nums)):
            if nums[i] == key:
                ind.append(i)
        final = set()
        for index in ind:
            final.add(index)
            for i in range(index,min(len(nums),index+k+1)):
                final.add(i)
            for j in range(index,max(index-k-1,-1),-1):
                final.add(j)
        return sorted(list(final))