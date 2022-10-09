# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        
        return self.traverse(root, {}, k)
    
    def traverse(self, root, mem, target):
        
        if root == None:
            return False
        
        if target - root.val in mem:
            return True
        else:
            mem[root.val] = True
        
        return self.traverse(root.left, mem, target) | self.traverse(root.right, mem, target)
        
            
        
    
    
    
#     def search(self, root, value):
        
#         if root == None:
#             return False
        
        
#         if root.val == value:
#             return True
#         elif root.val < value:
#             return self.search(root.right, value)
#         elif root.val > value:
#             return self.search(root.left, value)
        
    
    