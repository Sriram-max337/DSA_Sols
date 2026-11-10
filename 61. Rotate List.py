# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def rotateRight(self, head: ListNode | None, k: int) -> ListNode | None:
        if not head or not head.next:
            return head

        node = head
        lst = ListNode()
        lst.next = head
        n = 0
        while node:
            n += 1
            node = node.next

        k = k % n
        node = lst.next
        for i in range(n-k-1):
            node = node.next
        
        lst.next = node.next
        node.next = None

        node = lst.next
        while node.next:
            node = node.next
        node.next = head

        return lst.next