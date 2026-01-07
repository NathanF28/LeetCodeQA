class Solution:
    def maxLevelSum(self, r: Optional[TreeNode]) -> int:
        return min((-sum(n.val for n in q),i) for i,q in enumerate(takewhile(bool,
            accumulate(count(),lambda q,_:[c for n in q for c in (n.left,n.right) if c],
                initial=[r]*bool(r))),1))[1]