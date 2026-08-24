# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        def flatten_tree(node):
            if not node:
                return
            l = node.left
            r = node.right
            flatten_tree(l)
            flatten_tree(r)
            if l:
                node.left = None
                node.right = l
                curr = node
                while curr.right:
                    curr = curr.right
                curr.right = r
        flatten_tree(root)