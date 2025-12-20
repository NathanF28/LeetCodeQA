# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:

        res = -float('inf')
        def dfs(node):
            nonlocal res
            if not node:
                return 0
            n = node.val
            l =  max(dfs(node.left),0)
            r =  max(dfs(node.right),0)
            c = n + l + r
            res = max(c,res)

            return n + max(l,r)



        dfs(root)
        return res
