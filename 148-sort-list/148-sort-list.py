# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
    
        new_list = []
        
        temp = head
        
        while temp != None:
            new_list.append(temp.val)
            temp = temp.next
        
        new_list.sort()
        temp = head
        
        for i in range(len(new_list)):
            
            temp.val = new_list[i]
            temp = temp.next
            
        return head    
    
    