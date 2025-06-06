class Solution:
    def robotWithString(self, s: str) -> str:
        freq = Counter(s)
        smallest = "a"
        stack = []
        res = ""
        for char in s:
            stack.append(char)
            freq[char]-=1
            
            while not freq[smallest] and smallest < "z":
                smallest = chr(ord(smallest)+1)

            while stack and stack[-1] <= smallest:
                res+= stack.pop() 
        
        return res

