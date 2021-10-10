# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.prev_sum = 0

    def convertBST(self, root: TreeNode) -> TreeNode:

        if root is None:
            return None
        
        root.right = self.convertBST(root.right)
        self.prev_sum += root.val
        root.val = self.prev_sum
        root.left = self.convertBST(root.left)


        
        

        return root