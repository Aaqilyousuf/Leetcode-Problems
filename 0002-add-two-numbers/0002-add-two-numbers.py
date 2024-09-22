# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        res = None
        rev_1 = None
        rev_2 = None
        while l1:
            node = l1.next
            l1.next = rev_1
            rev_1 = l1
            l1 = node
        while l2:
            node = l2.next
            l2.next = rev_2
            rev_2 = l2
            l2 = node
        sum1 = 0
        sum2 = 0
        curr1, curr2 = rev_1, rev_2
        while curr1:
            sum1 =(sum1*10) + curr1.val
            curr1 = curr1.next
        while curr2:
            sum2 =(sum2*10) + curr2.val
            curr2 = curr2.next
           
        tot = sum1+sum2
        if tot == 0:
            return ListNode(0)
        totli = list(str(tot))
        for n in totli:
            node = ListNode(int(n))
            node.next = res
            res = node
        return res



        
        