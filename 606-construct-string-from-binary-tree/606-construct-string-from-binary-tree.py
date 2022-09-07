# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
    
        lis = []
        self.b_to_str(root, lis)
        
        return ''.join(lis)
    
    def b_to_str(self, root, lis):
        
        if root == None:
            return None
        
        lis.append(str(root.val))
        
        lis.append("(")
        l = self.b_to_str(root.left, lis)
        lis.append(")")
        
        # if l == None:
        #     lis.pop()
        #     lis.pop()
        
        lis.append("(")
        r = self.b_to_str(root.right, lis)
        lis.append(")")
        
        
        if r == None and l != None:
            lis.pop()
            lis.pop()
        
        if l == None and r == None:
            lis.pop()
            lis.pop()
            lis.pop()
            lis.pop()
            
        return root
        
        
    