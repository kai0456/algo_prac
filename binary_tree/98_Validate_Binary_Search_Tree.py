# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        self.vec =[]
        self.build_increasing_vec(root)
        for i in range(1, len(self.vec)):
            if self.vec[i] <= self.vec[i-1]:
                return False

        return True

    def build_increasing_vec(self,root):
        if root is None:
            return

        self.build_increasing_vec(root.left)
        self.vec.append(root.val)
        self.build_increasing_vec(root.right)