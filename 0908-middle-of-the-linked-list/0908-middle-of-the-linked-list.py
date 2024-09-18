# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def length(head):
            count = 0
            while head:
                count += 1
                head = head.next
            return count
        l = length(head)
        curr = head
        c = 0
        while curr:
            c += 1
            if c == (l//2)+1:
                head = curr
            else:
                curr = curr.next
        return head