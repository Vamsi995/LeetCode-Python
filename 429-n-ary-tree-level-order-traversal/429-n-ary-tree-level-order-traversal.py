"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        
        if root == None:
            return None
        
        queue = [root]
        ans = [[root.val]]
        
        while len(queue) != 0:
            
            a = len(queue)
            temp = []
            for i in range(a):
                
                curr = queue.pop(0)
                
                for c in curr.children:
                    
                    if c != None:
                        temp.append(c.val)
                        queue.append(c)
            
            if len(temp) != 0:
                ans.append(temp.copy())
            
        return ans
        
        
        
        
        