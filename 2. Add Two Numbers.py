# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        n1, n2 = "",""
        x,y = l1,l2
        
        while x:
            n1 += str(x.val)
            x = x.next

        while y:
            n2 += str(y.val)
            y = y.next

        no = int(n1[::-1]) + int(n2[::-1])
        lst = [int(d) for d in str(no)][::-1]

        head = ListNode(lst[0])
        curr = head
        for i in lst[1:]:
            curr.next = ListNode(i)
            curr = curr.next
        return head