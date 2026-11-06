#Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists: list[ListNode | None]) -> ListNode | None:
        if not lists:
            return 

        def DC(lst):
            if not lst:
                return
            if len(lst) == 1:
                return lst[0]
            
            mid_idx = len(lst)//2
            left = lst[:mid_idx]
            right = lst[mid_idx:]

            left_merged = DC(left)
            right_merged = DC(right)

            return mergeTwoLists(left_merged, right_merged)

        def mergeTwoLists(lst1, lst2):
            dummy_ll = ListNode()
            tail = dummy_ll
            l = lst1
            r = lst2
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
            return dummy_ll.next

        return DC(lists)