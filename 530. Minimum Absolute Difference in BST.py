# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        min_diff = float("inf")
        prev = None

        def ino(node):
            nonlocal min_diff, prev
            if not node:
                return

            ino(node.left)
            if prev is not None:
                min_diff = min(min_diff, node.val - prev)
            prev = node.val
            ino(node.right)
        ino(root)

        return min_diff