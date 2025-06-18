# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        #first find the mid and rverse that second part and compare that
        slow = head
        fast = head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        #now slow is the mid we have to reverse from the mid to end and compare

        node =  None
        while slow:
            temp = slow.next
            slow.next = node
            node = slow
            slow = temp
        #now the second half is reversed slow = 1->2
        first = head #1->2->2->1
        second = node #1->2
        
        while first and second:
            if first.val != second.val:
                return False
            first = first.next
            second = second.next
        return True
