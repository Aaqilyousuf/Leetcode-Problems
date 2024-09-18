# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = head
        curr = head
        while curr and curr.next:
            curr = curr.next
            if curr.val == prev.val:
                prev.next = curr.next
            else:
                prev = prev.next
        return head


        