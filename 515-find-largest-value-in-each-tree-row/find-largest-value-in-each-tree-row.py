# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        def bfs(curr_level, result):
            if not curr_level:
                return result 
            next = []
            curr = []
            maxe = -float('inf')
            for node in curr_level:
                curr.append(node)
                maxe = max(maxe,node.val)
                if node.left:
                    next.append(node.left)
                if node.right:
                    next.append(node.right)
            result.append(maxe)
            return bfs(next,result)
        return bfs([root],[]) if root else []