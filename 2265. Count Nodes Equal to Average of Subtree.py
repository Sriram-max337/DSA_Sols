# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        if not root:
            return
        node_count = 0
        def equaltoavg(node):
            nonlocal node_count
            if not node:
                return 0,0
            tot_n = 1
            tot_sumn = node.val
            left_n,left_sumn = equaltoavg(node.left)
            right_n, right_sumn = equaltoavg(node.right)
            tot_n += left_n + right_n
            tot_sumn += left_sumn + right_sumn
            if node.val == tot_sumn//tot_n:
                node_count += 1
            return tot_n, tot_sumn
        equaltoavg(root)
        return node_count