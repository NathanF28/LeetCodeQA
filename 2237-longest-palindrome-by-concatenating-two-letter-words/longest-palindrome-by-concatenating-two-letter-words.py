class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        evens = defaultdict(int)
        map = defaultdict(int)
        count = 0
        for word in words:
            if len(set(word)) == 1:
                evens[word]+=1
                continue
            need = word[::-1]
            if need in map:
                count+=4
                map[need]-=1
                if map[need] == 0:
                    del map[need]
            else:
                map[word]+=1
        flag = True
        for key,value in evens.items():
            if value & 1:
                flag = False
                count+= 2 * (value-1)
            else:
                count+= 2 * value
        return count+2 if not flag else count