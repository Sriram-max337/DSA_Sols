# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        def ConsTree(preorder, inorder):
            if not preorder or not inorder:
                return
            root = preorder[0]
            mid = inorder.index(root)
            node = TreeNode(root)
            lin = inorder[:mid]
            rin = inorder[mid+1:]
            lpre = preorder[1:mid+1]
            rpre = preorder[mid+1:]
            node.left = ConsTree(lpre, lin)
            node.right = ConsTree(rpre,rin)
            return node
        return ConsTree(preorder, inorder)