# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:
        self.vec = []

        self.traverse(root)

        min_val = math.inf
        for i in range(1, len(self.vec)):
            diff = abs(self.vec[i] - self.vec[i-1])
            if diff < min_val:
                min_val = diff

        return min_val



    def traverse(self, root):
        if root is None:
            return

        self.traverse(root.left)
        self.vec.append(root.val)
        self.traverse(root.right)

