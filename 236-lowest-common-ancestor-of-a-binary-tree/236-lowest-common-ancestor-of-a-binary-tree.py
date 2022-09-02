# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        return self.lca(root, p, q)
    
    def lca(self, root, p, q):
        
        if root.val == p.val or root.val == q.val:
            return root
        
        if root == None:
            return None
        
        l = None
        r = None
        if root.left:
            
            l = self.lca(root.left, p, q)
        
        if root.right:
            
            r = self.lca(root.right, p, q)
            
        if r != None and l != None:
            return root
        
        if r == None:
            return l
        else:
            return r
        
            
        
        
        