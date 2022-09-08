# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        
        if head.next == None:
            return True
        
        slow = head
        fast = head
        
        prev = None
        nex = slow.next
        count = 0
        while fast != None and fast.next != None:
            
            fast = fast.next.next
            slow.next = prev
            prev = slow
            slow = nex
            nex = nex.next
            count += 1
            
        
        l_head = prev
        
        temp = slow
        c = 0
        while temp != None:
            c += 1
            temp = temp.next
            
        r_head = None
        if (c + count) % 2 == 0:
            r_head = slow
        else:
            r_head = slow.next

        
        while l_head != None and r_head != None:
            
            if l_head.val != r_head.val:
                return False
            
            l_head = l_head.next
            r_head= r_head.next
        
        return True