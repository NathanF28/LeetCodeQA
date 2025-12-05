class Solution:
    def countCollisions(self, directions: str) -> int:
        # Finite automat definition:
        # for each 'state'+'input' define (action, next state)
        fa = {
            ('L','L'):(0,'L'), ('L','R'):(2,'R'), ('L','S'):(0,'S'),
            ('S','L'):(1,'S'), ('S','R'):(2,'R'), ('S','S'):(0,'S'),
            ('R','L'):(3,'S'), ('R','R'):(2,'R'), ('R','S'):(4,'S')
        }
        state,rc,ans = 'L', 0, 0
        for inp in directions:
            act,state = fa[(state,inp)]
            if   act == 1: ans += 1
            elif act == 2: rc  += 1
            elif act == 3: ans += rc+1;  rc = 0
            elif act == 4: ans += rc;    rc = 0
        return  ans
        