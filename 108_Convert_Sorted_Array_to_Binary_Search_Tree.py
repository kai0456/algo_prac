# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        # [0,1,2,3,4,5]

        if len(nums) == 0:
            return None

        left = 0
        right = len(nums) - 1
        mid = (left + right) // 2

        root = TreeNode(val = nums[mid])
        left = self.sortedArrayToBST(nums[left:mid])
        right = self.sortedArrayToBST(nums[mid+1:])

        root.left = left
        root.right = right

        return root

