# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def check_nodes(self, l, r):
        if not l and not r:
            return True
        
        if not l or not r:
            return False
        if l.val != r.val:
            return False
        
        return self.check_nodes(l.left, r.right) and self.check_nodes(l.right, r.left)
        
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        l = root.left
        r = root.right
        
        return self.check_nodes(l,r)