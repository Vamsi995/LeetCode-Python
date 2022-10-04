# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
    
        return self.find_sum(root, targetSum, 0)
    
    
    def find_sum(self, root, target, count):
        
        if root == None:
            return False
        
        ans = False
        
        count += root.val
        ans |= self.find_sum(root.left, target, count)
        ans |= self.find_sum(root.right, target, count)
        
        if root.left == None and root.right == None:
            if count == target:
                return True
        
        return ans
        
        
    
    
    
    
    