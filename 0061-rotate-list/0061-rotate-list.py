# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # if head == None or head.next == None:
        #     return head
        
        # for _ in range(k):
        #     temp = head
        #     while temp.next.next:
        #         temp = temp.next
        #     end = temp.next
        #     temp.next = None
        #     end.next = head
        #     head = end
        # return head
        #optimal sol:
        if head == None or head.next == None or k == 0:
            return head
        temp = head
        length = 1
        while temp.next:
            length += 1
            temp = temp.next
        k = k % length
        if k == 0:
            return head
        temp.next = head #make it as circular LL
        noOfMoves = length - k
        temp = head
        for _ in range(noOfMoves - 1):
            temp = temp.next
        new_head = temp.next
        temp.next = None

        return new_head
        