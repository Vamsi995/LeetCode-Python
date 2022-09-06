# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        final_len = 0
        
        temp = l1
        l1_len = 0
        l2_len = 0
        
        while temp != None:
            temp = temp.next
            l1_len += 1
        
        temp = l2
        while temp != None:
            temp = temp.next
            l2_len += 1
        
        if l1_len > l2_len:
            final_len = l1_len
            temp_l1 = l1
            temp_l2 = l2
        else:
            final_len = l2_len
            temp_l1 = l2
            temp_l2 = l1
        
        new_list = ListNode(0)
        temp = new_list
        for i in range(1, final_len):
            temp.next = ListNode(0)
            temp = temp.next
        
        
        temp_l3 = new_list
        carry = 0

        while temp_l1 != None:
            
            if temp_l2 != None:
                temp_l3.val = (carry + temp_l1.val + temp_l2.val) % 10
                carry =  (carry + temp_l1.val + temp_l2.val) // 10
                temp_l2 = temp_l2.next

            else:
                if carry == 1:
                    temp_l3.val = (carry + temp_l1.val) % 10
                    carry =  (carry + temp_l1.val) // 10
                else:
                    temp_l3.val = temp_l1.val
                
                
            temp_l1 = temp_l1.next
            
            if temp_l3.next == None and carry == 1:
                temp_l3.next = ListNode(1)
                temp_l3 = temp_l3.next
            temp_l3 = temp_l3.next    
            
        return new_list     
            
        
        
        
        
        