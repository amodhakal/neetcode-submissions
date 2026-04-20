# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        data = []

        current = head
        while current is not None:
            next = current.next
            current.next = None
            data.append(current)
            current = next

        if len(data) == 0:
            return None

        newhead = data[len(data) - 1]
        current = newhead
        for idx in range(len(data) -2, -1, -1):
            current.next = data[idx]
            current = current.next

        return newhead


        