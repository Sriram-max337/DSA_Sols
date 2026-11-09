# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: ListNode | None, x: int) -> ListNode | None:
        node = head
        Sll = ListNode()
        Lll = ListNode()
        t1 = Sll
        t2 = Lll

        while node:
            if node.val >= x:
                t2.next = node
                t2 = t2.next
            else:
                t1.next = node
                t1 = t1.next

            node = node.next

        t2.next = None
        t1.next = Lll.next
        return Sll.next