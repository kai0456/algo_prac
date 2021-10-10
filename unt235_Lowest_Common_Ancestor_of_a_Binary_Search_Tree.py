# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root is None:
            return

        if root == p or root == q:
            return root

        if root.val >= min(p.val, q.val) and root.val < max(p.val, q.val):
            return root
        elif root.val < min(p.val, q.val):
            return self.lowestCommonAncestor(root.right, p, q)
        elif root.val >= max(p.val, q.val):
            return self.lowestCommonAncestor(root.left, p, q)