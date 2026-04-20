# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# 0 > 1 > 2 > 3 > 4
# >
# 1 > 2 > 3 > 4
# > 0
# 2 > 3 > 4
# 1 > 0

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        truhead = head
        falsehead = ListNode()
        while truhead is not None:
            truval = truhead.val
            newitem = ListNode(truval, falsehead.next)
            falsehead.next = newitem

            truhead = truhead.next

        return falsehead.next
