# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        def ConsTree(postorder, inorder):
            if not inorder or not postorder:
                return 
            root = postorder[-1]
            mid = inorder.index(root)
            node = TreeNode(root)
            lin = inorder[:mid]
            rin = inorder[mid+1:]
            lpo = postorder[:mid]
            rpo = postorder[mid:-1]
            node.left = ConsTree(lpo, lin)
            node.right = ConsTree(rpo, rin)
            return node
        return ConsTree(postorder, inorder)