# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        
        self.prune(root)
                
        if root.left == None and root.right == None:
            if root.val == 0:
                return None
        return root
    
    
    def prune(self, root):
        
        if root == None:
            return None

        l = self.prune(root.left)
        r = self.prune(root.right)
        # print(root.val, l, r)
        
        if l == None and r == None:
            return root.val
        
        if l == None:
            if r == 0:
                root.right = None
                return root.val
            return r
        
        if r == None:
            if l == 0:
                root.left = None
                return root.val
            return l
        
        if l == 0:
            root.left = None
            
        if r == 0:
            root.right = None
        
        return max(l, r, root.val)
        
        
        
        