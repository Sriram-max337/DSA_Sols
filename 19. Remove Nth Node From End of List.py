class Solution:
    def removeNthFromEnd(self, head, n):
        l = head
        r = head
        for i in range(n+1):
            if r is None:
                return head.next
            r = r.next

        while r:
            l = l.next
            r = r.next

        l.next = l.next.next
        return head