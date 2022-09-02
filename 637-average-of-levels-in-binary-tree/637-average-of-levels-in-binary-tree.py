# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        
        avg = []
        
        queue = [root]
        
        while len(queue) != 0:
            
            a = len(queue)
            mean = 0
            for i in range(a):
                curr = queue.pop(0)
                
                if curr.left:
                    queue.append(curr.left)
                
                if curr.right:
                    queue.append(curr.right)
                
                mean += curr.val
                
            avg.append(mean/a)

        return avg
        
        
        
        
        