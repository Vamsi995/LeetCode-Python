# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        start = 0
        end = len(lists) - 1
        
        if len(lists) == 0:
            return None
        
        if len(lists) == 1:
            return lists[0]
        
        
        interval = 2
        
        while len(lists) != 1:
    
            temp = []
            for i in range(0, len(lists), interval):
                
                lis = lists[i:i+interval]
                if i + interval > len(lists):
                    temp.append(lists[i])
                else:
                    temp.append(self.mergeTwoSorted(lis[0], lis[1]))

            lists = temp.copy()
            
        return lists[0]
            
    
    def mergeTwoSorted(self, head1, head2):
        
        # print(head1, head2)
            
        temp1 = head1
        temp2 = head2
        
        while temp1 != None and temp2 != None:
            
            if temp1.val < temp2.val:
                prev = temp1
                while temp1 and temp2 and temp1.val <= temp2.val:
                    prev = temp1
                    temp1 = temp1.next
                
                
                prev.next = temp2

            
            else:
                prev = temp2
                while temp1 and temp2 and temp2.val <= temp1.val:
                    prev = temp2
                    temp2 = temp2.next
                
                prev.next = temp1
        
        
        if head1 == None and head2 == None:
            return None
        
        elif head1 == None:
            return head2
        elif head2 == None:
            return head1
        
        
        if head1.val < head2.val:
            return head1
        else:
            return head2
        
        
        
        
        
        