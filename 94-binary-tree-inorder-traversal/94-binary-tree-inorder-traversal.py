# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        lis = []
        self.inorder(root, lis)
        
        return lis
        
    def inorder(self, root, lis):        
        
        if root == None:
            return root
        
        
        self.inorder(root.left, lis)
        lis.append(root.val)
        self.inorder(root.right, lis)