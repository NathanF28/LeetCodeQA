class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        n = len(blocks)
        minimum = n
        map = Counter(blocks[:k])
        minimum = map["W"] if "W" in map else 0
        l = 0
        for i in range(k,n):
            if blocks[i] not in map:
                map[blocks[i]]=1
            else:
                map[blocks[i]]+=1
            if map[blocks[l]] > 1:
                map[blocks[l]]-=1
            else:
                del map[blocks[l]]
            minimum = min(map["W"],minimum)
            l+=1
        return minimum
