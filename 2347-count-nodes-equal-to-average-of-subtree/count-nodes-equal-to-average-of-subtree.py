# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        count = 0
        def dfs(node):
            nonlocal count
            if not node:
                return (0,0)
            
            l_sum, l_count = dfs(node.left)
            r_sum, r_count = dfs(node.right)

            t_sum = l_sum  + r_sum + node.val
            t_count = 1 + r_count + l_count
            if t_sum // t_count == node.val:
                count+=1
            return (t_sum,t_count)
        dfs(root)
        return count

        