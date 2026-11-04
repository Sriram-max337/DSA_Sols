class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sortedArrayToBST(self, nums: list[int]) -> TreeNode | None:
        node = TreeNode()
        def BuildTree(lst, node):
            if not lst:
                return

            root_idx = len(lst)//2
            root = lst[root_idx]
            left_subt = lst[:root_idx]
            right_subt = lst[root_idx+1:]
            node = TreeNode(root)

            if left_subt:
                node.left = BuildTree(left_subt, node)
            if right_subt:
                node.right = BuildTree(right_subt, node)
            return node
             
        return BuildTree(nums, node)