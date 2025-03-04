class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        map =  {} 
        sume = 0
        for answer in answers:
            if answer in map:
                map[answer] -=1
                if map[answer] == -1:
                    del map[answer]
            if answer not in map:
                map[answer] = answer
                sume+= answer+1
        return sume
                
        