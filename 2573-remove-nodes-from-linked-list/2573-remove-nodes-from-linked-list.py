# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNodes(self, head: ListNode) -> ListNode:
        stack = []
        current = head

        
        while current:
            
            while stack and stack[-1].val < current.val:
                stack.pop()
            stack.append(current)
            current = current.next

        
        dummy = ListNode(0)
        current = dummy
        for node in stack:
            current.next = ListNode(node.val)
            current = current.next

        return dummy.next
