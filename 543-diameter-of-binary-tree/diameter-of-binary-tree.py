# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        die = 0
        def dfs(node):
            nonlocal die
            if not node:
                return 0

            left  = dfs(node.left)
            right = dfs(node.right)
            curr = max(left,right)
            die = max(left+right,die)
            return curr + 1
            
        dfs(root)
        return die

