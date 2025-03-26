# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        def left_max(node):
            if not node.right:
                return node
            return left_max(node.right)
        def delete(node,target):
            if not node:
                return None
            if node.val > target:
                node.left = delete(node.left,target)
            elif node.val < target:
                node.right = delete(node.right,target)
            else:
                if not node.left and not node.right:
                    return None
                
                if not node.left:
                    return node.right
                if not node.right:
                    return node.left

                change = left_max(node.left)
                node.val = change.val
                node.left  = delete(node.left,change.val) 
            return node

        return delete(root,key)
        