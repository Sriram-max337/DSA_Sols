# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def Tsum(self, curr_sum, root, targetSum):
        if not root:
            return
        
        curr_sum += root.val
        if not root.left and not root.right:
            if curr_sum == targetSum:
                return True
            else:
                False

        return self.Tsum(curr_sum, root,targetSum)
        
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        curr_sum = 0

        return self.Tsum(curr_sum,root, targetSum)