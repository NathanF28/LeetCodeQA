# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        if not root:
            return 0
        def bfs(nodes,level):
            next = [] 
            for node in nodes:
                if node.left:
                    next.append(node.left)
                if node.right:
                    next.append(node.right)
            if next:
                return bfs(next,level+1)
            return level
        return bfs([root],1)
