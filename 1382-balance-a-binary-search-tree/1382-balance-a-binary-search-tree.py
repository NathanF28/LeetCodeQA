# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        inorder = [] 
        def getlist(root):
            nonlocal inorder 
            if not root:
                return
            getlist(root.left)
            inorder.append(root.val)
            getlist(root.right)

        def buildtree(liste):
            if len(liste) == 0:
                return None
            mid = len(liste) // 2
            root = TreeNode(liste[mid])
            root.left = buildtree(liste[:mid])
            root.right= buildtree(liste[mid+1:])
            return root
        getlist(root)
        return buildtree(inorder)
            
        