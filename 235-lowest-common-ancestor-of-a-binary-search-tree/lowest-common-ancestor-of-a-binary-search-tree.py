# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if p.val >= q.val:
            p,q = q,p
        def dfs(node):
            if p.val <= node.val <= q.val:
                return node
            if node.val > q.val:
                return dfs(node.left)
            else:
                return dfs(node.right)
        return dfs(root)
        