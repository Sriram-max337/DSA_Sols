# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution: 
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def hdiff(root):
            if not root:
                return 0

            max_left = hdiff(root.left)
            max_right = hdiff(root.right)

            if max_left == -1 or max_right == -1:
                return -1

            if abs(max_left - max_right) > 1:
                return -1
            else:
                return 1 + max(max_left, max_right)
        
        if hdiff(root) == -1:
            return False
        else:
            return True