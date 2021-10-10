# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        q = collections.deque()
        
        vec = []
        res = []
        
        
        if root: q.append(root)
            
        while q:
            q_size = len(q)
            
            for i in range(q_size):
                node = q.popleft()
                
                if node:
                    vec.append(node.val)
                    if node.left : q.append(node.left)
                    if node.right: q.append(node.right)
            elem = vec[-1]
            
            res.append(elem)
        
        return res
                    
        