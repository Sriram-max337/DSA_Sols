# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        ps = 0
        def path_sum(node, cs):
            nonlocal ps
            if not node:
                return 0

            cs += str(node.val)
            if not node.left and not node.right:
                ps += int(cs)

            path_sum(node.left, cs)
            path_sum(node.right, cs)
            
        path_sum(root, "")
        return ps