# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        
        first = head
        second = head
        
        for i in range(n):
            first = first.next
        
        prev = head
        while first:
            first = first.next
            prev = second
            second = second.next
         
        if second == head:
            head = head.next
            return head
        
        nex = second.next
        prev.next = nex
        del second
        return head
        
        