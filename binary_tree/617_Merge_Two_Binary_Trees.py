# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: TreeNode, root2: TreeNode) -> TreeNode:

        node = TreeNode(None)

        if root1 is None and root2 is None:
            return

        if root1 and root2 is None:
            node.val = root1.val
            node.left = self.mergeTrees(root1.left, None)
            node.right = self.mergeTrees(root1.right, None)
        elif root1 is None and root2:
            node.val = root2.val
            node.left = self.mergeTrees(None, root2.left)
            node.right = self.mergeTrees(None,root2.right)
        elif root1 and root2:
            node.val = root1.val + root2.val
            node.left = self.mergeTrees(root1.left, root2.left)
            node.right = self.mergeTrees(root1.right, root2.right)


        return node