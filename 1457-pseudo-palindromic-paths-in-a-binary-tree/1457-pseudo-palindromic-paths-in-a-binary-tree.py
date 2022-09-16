# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        
        count = 0
    
        def count_palindrome(root, mem):
            nonlocal count
            
            # print(mem)
            if root == None:
                return None


            mem[root.val] = 1 + mem.get(root.val, 0)

            if mem[root.val] % 2 != 0:
                mem["odd"] = 1 + mem.get("odd", 0)
            else:
                mem["odd"] -= 1


            if root.left == None and root.right == None:

                if mem["odd"] == 1 or mem["odd"] == 0:
                    count += 1
                    
                if root.val in mem:
                    mem[root.val] -= 1
                    if mem[root.val] % 2 == 0:
                        mem["odd"] -= 1
                    else:
                        mem["odd"] += 1

                return None

            count_palindrome(root.left, mem)
            count_palindrome(root.right, mem)
            
            # print(root.val)
            if root.val in mem:
                if mem[root.val] > 0:
                    mem[root.val] -= 1
                    if mem[root.val] % 2 == 0:
                        mem["odd"] -= 1
                    else:
                        mem["odd"] += 1
    
        count_palindrome(root, {})
        
        return count