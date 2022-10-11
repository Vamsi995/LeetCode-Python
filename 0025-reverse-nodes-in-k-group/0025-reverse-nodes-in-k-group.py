# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    
    def reverseList(self, head):
        
        temp = head
        prev = None
        curr = head
        n = curr.next
        
        while curr != None:
            
            curr.next = prev
            prev = curr
            curr = n
            if curr != None:
                n = curr.next
        
        return (head, prev)
        
    
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        
        temp = head
        temper = head
        prev = head
        counter = 0
        
        res = []
        l = 0
        
        prev_head_tail = (None, None)
        main_head = None
        while temp != None:
            prev = temp
            temp = temp.next
            counter += 1
            l += 1
            
            if counter == k:
                prev.next = None
                t = self.reverseList(temper)
                if prev_head_tail == (None, None):
                    main_head = t[1]
                else:
                    prev_head_tail[0].next = t[1]
                prev_head_tail = (t[0], t[1])
                
                temper = temp
                counter = 0

            
            
        if l % k != 0:
            prev_head_tail[0].next = temper
        
#         h = res[0][1]
        
#         for i in range(len(res) - 1):
            
#             res[i][0].next = res[i+1][1]
            
        return main_head
        
        
        
        
        