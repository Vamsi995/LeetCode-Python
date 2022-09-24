# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        
        curr_sum = 0
        ans = []
        final = []
        
        self.find_path(root, curr_sum, ans, targetSum, final)
        return final
        
    def find_path(self, root, curr_sum, ans, target, final):
        
        if root == None:
            return None
    
        ans.append(root.val)
        
        self.find_path(root.left, curr_sum + root.val, ans, target, final)
        self.find_path(root.right, curr_sum + root.val, ans, target, final)
        
        if root.left == None and root.right == None:
            if target == curr_sum + root.val:
                final.append(ans.copy())
        
        ans.pop()
        
        