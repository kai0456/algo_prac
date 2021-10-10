# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if root is None:
            return None

        if key > root.val:
            root.right = self.deleteNode(root.right, key)
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)
        else:
            # key == root.val
            if root.left and root.right is None:
                return root.left
            elif root.right and root.left is None:
                return root.right
            elif root.right is None and root.left is None:
                del root
                return None
            else:
                # if both children exist
                # then: replace the root by the minimum node on the right subtree and return the new node
                node = TreeNode(self.findMin(root.right).val)
                node.left = root.left
                node.right = self.deleteNode(root.right, node.val)
                return node
        return root

    def findMin(self, node):
        # print(node.val)
        if node is None:
            return

        if node.left:
            node = self.findMin(node.left)

        return node




