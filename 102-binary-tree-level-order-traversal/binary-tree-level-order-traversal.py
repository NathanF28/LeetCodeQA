# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        def bfs(curr_level, result):
            if not curr_level:
                return result
            next_level = []
            curr_to_result = []  #  to be appended to result
            for node in curr_level:
                curr_to_result.append(node.val)
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            result.append(curr_to_result)
            return bfs(next_level,result)
        return bfs([root],[]) if root else []
