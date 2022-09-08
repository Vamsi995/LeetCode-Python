# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
one_way = ""
other_way = ""
class Solution:
    def isPalindrome(this, head):
        global one_way
        global other_way
        one_way = one_way + str(head.val)
        other_way  = str(head.val) + other_way
        # print(one_way, other_way)
        if head.next == None:
            ans = one_way == other_way
            one_way = ""
            other_way = ""
            return ans
        return this.isPalindrome(head.next)