# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        cur1 = headA
        cur2 = headB
        while cur1 != cur2:
            cur1 = headB if cur1==None else cur1.next
            cur2 = headA if cur2==None else cur2.next
        return cur1