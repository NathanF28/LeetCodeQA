# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(node):
            if not node:
                return None,0
            left,lh = dfs(node.left)
            right,rh = dfs(node.right)

            if lh == rh:
                return node, lh+1
            elif lh > rh:
                return left, lh+1
            elif lh < rh:
                return right, rh+1
        x , _ = dfs(root)
        return x


        
