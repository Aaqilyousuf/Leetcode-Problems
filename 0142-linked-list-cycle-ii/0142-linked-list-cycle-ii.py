# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        big = head
        baby = head
        if head == None or head.next == None:
            return None
       
        while big and big.next:
            big = big.next.next
            baby = baby.next
            if big == baby:
                baby = head
                while baby != big:
                    baby = baby.next
                    big = big.next
                return baby
        return None
        

        