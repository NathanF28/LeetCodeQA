class Solution:
    def equalFrequency(self, word: str) -> bool:
        for i in range(len(word)):
            check =  word[:i] + word[i+1:] 
            map = Counter(check)
            check = set()
            for key,value in map.items():
                check.add(value)
            if len(check) == 1:
                return True
        return False