# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return 
        new_list = None
        curr = head
        while curr:
            nNode = curr.next
            curr.next = new_list
            new_list = curr
            curr = nNode
        return new_list

        