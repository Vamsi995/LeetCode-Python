# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        count = 0
        max_path_val = 0
        
        if root != None:
            count = 1
        
    
        def dfs(root, max_path_val):
            nonlocal count
            
            if root == None:
                return None
            
            if root.left:
                if root.left.val >= max_path_val:
                    count += 1
                dfs(root.left, max(max_path_val, root.left.val))
            
            if root.right:
                if root.right.val >= max_path_val:
                    count += 1
                
                dfs(root.right, max(max_path_val, root.right.val))
        
        
        dfs(root, root.val)
        return count
            
            
        
    
    
    
    
    