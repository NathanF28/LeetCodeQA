# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        def bfs(curr_level, result, direction):
            if not curr_level:
                return result
            next = []
            curr = []
            for node in curr_level:
                print(node)
                curr.append(node.val)
                if node.left:
                    next.append(node.left)
                if node.right:
                    next.append(node.right)
            if direction == -1:
                result.append(curr)
            else:
                result.append(curr[::-1])
            direction*=-1
            return bfs(next,result,direction)
        return bfs([root], [], -1) if root else []
        