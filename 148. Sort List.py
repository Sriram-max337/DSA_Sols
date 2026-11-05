# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def sortList(self, head: ListNode | None) -> ListNode | None:
        if not head:
            return 

        sorted_ll = ListNode()
        
        def SortLL(node):
            if not node or not node.next: 
                return node
                
            sp_prev = node
            sp = node
            fp = node
            while sp and fp and fp.next:
                sp_prev = sp
                sp = sp.next
                fp = fp.next.next
            sp_prev.next = None
            
            left = SortLL(node)
            right = SortLL(sp)
            
            def mergeTwoLists(list1: ListNode | None, list2: ListNode | None) -> ListNode | None:
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
                
            return mergeTwoLists(left, right) 
            
        return SortLL(head) 