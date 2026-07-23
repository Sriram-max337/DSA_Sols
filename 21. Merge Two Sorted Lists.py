# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        lst = ListNode()
        tail = lst
        l = list1
        r = list2

        while l and r:
            if l.val <= r.val:
                tail.next = l
                l = l.next
            else:
                tail.next = r
                r = r.next
            tail = tail.next

        if l:
            tail.next = l
        else:
            tail.next = r

        return lst.next