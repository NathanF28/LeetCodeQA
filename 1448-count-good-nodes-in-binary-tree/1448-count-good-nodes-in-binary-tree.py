# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # we traverse val = max(val, root.val) val > root.val 
        ans = 0

        def dfs(root, prev):
            nonlocal ans
            if not root: return 0
            prev = max(prev, root.val)
            if prev <= root.val:
                ans += 1

            # root, prev
            dfs(root.left, prev)
            dfs(root.right, prev)

            return ans

        return dfs(root, root.val)
