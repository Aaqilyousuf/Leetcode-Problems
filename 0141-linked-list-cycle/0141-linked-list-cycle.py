# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        baby = head
        big = head
        if(head == None):
            return False
        if big.next == None or big.next.next == None:
            return False
        big = big.next.next
        baby = baby.next

        while big!=baby:
            if big.next == None or big.next.next == None:
                return False
            big = big.next.next
            baby = baby.next
        return True
        