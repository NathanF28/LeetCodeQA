class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        mapp = {
            2 : ["a","b","c"],
            3 : ["d","e","f"],
            4 : ["g","h","i"],
            5 : ["j","k","l"],
            6 : ["m","n","o"],
            7 : ["p","q","r","s"],
            8 : ["t","u","v"],
            9 : ["w","x","y","z"]
        }
        possible = []
        def backtrack(index,string):
            if index == len(digits):
                possible.append(string)
                return
            for char in mapp[int(digits[index])]:
                string+= char
                backtrack(index+1,string)
                string = string[:-1]

        backtrack(0,"") if len(digits) else None 
        return possible