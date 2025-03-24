# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        diff = 0
        def dfs(node,_max,_min):
            nonlocal diff
            if not node:
                diff = max(diff,_max-_min)
                return
            _max = max(_max,node.val)
            _min = min(_min,node.val)
            dfs(node.left,_max,_min)
            dfs(node.right,_max,_min)
        dfs(root,root.val,root.val)
        return diff