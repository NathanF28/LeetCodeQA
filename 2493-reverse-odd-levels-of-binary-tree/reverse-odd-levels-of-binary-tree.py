# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def bfs(curr_level, odd):
            if not curr_level:
                return root 
            next_level = []
            for node in curr_level:
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            n = len(next_level)
            if odd == -1:
                for i in range(n//2):
                    next_level[i].val,next_level[n-i-1].val = next_level[n-i-1].val,next_level[i].val
            odd*=-1
            return bfs(next_level,odd)
        return bfs([root], -1) if root else None
        