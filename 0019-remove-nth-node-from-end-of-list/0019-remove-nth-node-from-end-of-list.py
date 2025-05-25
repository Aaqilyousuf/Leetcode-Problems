# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr = head
        tot = 0
        while curr:
            tot += 1
            curr = curr.next
        if n == 1 and tot == 1:
            return None
        currPos = tot - n
        if currPos == 0:
            return head.next
        curr1 = head
        for i in range(currPos-1):
            curr1 = curr1.next
        curr1.next = curr1.next.next

        return head
