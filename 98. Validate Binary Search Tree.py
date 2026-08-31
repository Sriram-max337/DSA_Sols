# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        prev = None
        def ino(node):
            nonlocal prev
            if not node:
                return True

            if not ino(node.left):
                return False
            if prev is not None and node.val <= prev:
                return False

            prev = node.val
            return ino(node.right)
            
        return ino(root)