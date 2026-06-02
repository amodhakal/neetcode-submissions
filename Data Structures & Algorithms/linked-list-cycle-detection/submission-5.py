# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        fast = head.next.next
        slow = head.next

        while None not in [ fast, slow]:
            if fast == slow:
                return True

            fastinter = fast.next
            if fastinter == None:
                return False

            fast = fastinter.next
            slow = slow.next
        
        return False
        