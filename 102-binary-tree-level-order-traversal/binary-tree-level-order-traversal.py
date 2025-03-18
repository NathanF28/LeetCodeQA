# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        def bfs(curr_level,result):
            if not curr_level:
                return result
            next = []
            curr = []
            for node in curr_level:
                curr.append(node.val)
                if node.left:
                    next.append(node.left)
                if node.right:
                    next.append(node.right)
            result.append(curr)
            return bfs(next,result)
        return bfs([root],[]) if root else []