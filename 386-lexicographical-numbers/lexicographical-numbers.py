class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        return (f:=lambda v:sum(([u,*f(u*10)] for u in range(v,v+10-(v==1)) if u<=n),[]))(1)