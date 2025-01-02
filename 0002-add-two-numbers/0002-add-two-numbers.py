# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if not l1 and not l2:
            return 
        if not l1:
            return l2
        if not l2:
            return l1
        cur1 = l1
        cur2 = l2
        list1 = []
        list2 = []
        while cur1:
            list1.append(cur1.val)
            cur1 = cur1.next
        while cur2:
            list2.append(cur2.val)
            cur2 = cur2.next
        num1 = int(''.join(map(str, list1[::-1])))
        num2 = int(''.join(map(str, list2[::-1])))
        result = num1 + num2        
        resL = list(map(int, str(result)[::-1]))
        finalRes = self.insert(resL)
        return finalRes
    def insert(self, resList):
        head = ListNode(resList[0])
        cur = head
        for i in range(1, len(resList)):
            newNode = ListNode(resList[i])
            cur.next = newNode
            cur = newNode
        return head


