# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
    
        mem = collections.defaultdict(list)
        self.inorder(root, 0, 0, mem)
        
        
        t = mem.items()
        
        t = sorted(t, key=lambda x: x[0])
        
        temp = {}

        for ind, it in t:
            it.sort()
            temp[ind[1]] = temp.get(ind[1], []) + it
            
            
        return [val for ind, val in sorted(temp.items(), key=lambda x: x[0])]
        
        
        
    
    def inorder(self, root, h, d, mem):
    
        
        if root == None:
            return None
        
        self.inorder(root.left, h-1, d+1, mem)
        self.inorder(root.right, h+1, d+1, mem)
        
        mem[(d, h)].append(root.val)
        
        
        
    