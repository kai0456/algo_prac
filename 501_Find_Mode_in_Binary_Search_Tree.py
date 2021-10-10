# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def findMode(self, root: TreeNode) -> List[int]:
        self.vec = []
        self.dfs(root)
        result = []
        
        
        max_count = 1
        count = 1
        result.append(self.vec[0])
        
        for i in range(1, len(self.vec)):
            if self.vec[i-1] == self.vec[i]:
                count +=1
            else:
                count = 1
            
            if count > max_count:
                max_count = count
                result.clear()
                result.append(self.vec[i])
            elif count == max_count:
                result.append(self.vec[i])
        
        # print(self.vec)
        
        return result
                
    
    def dfs(self, root) -> List[int]:
        if root is None: return
        
        self.dfs(root.left)
        self.vec.append(root.val)
        self.dfs(root.right)
