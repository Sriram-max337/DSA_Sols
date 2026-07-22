# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        lst = []
        curr = head
        while curr:
            lst.append(curr.val)
            curr = curr.next
        
        lst.reverse()
        curr = head
        for l in lst:
            curr.val = l
            curr = curr.next
        
        return head