# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        # if not head:
        #     return
        # n = 0
        # res = 0
        # t = head
        # while t and t.next:
        #     t = t.next
        #     n += 1
        # if n==1:
        #     return head.val + head.next.val
        # cur = head
        # for i in range(n//2):
        #     d = n-1-i
        #     dummy = cur.next
        #     for i in range(d):
        #         if dummy:
        #             dummy = dummy.next
                
        #     s = cur.val+dummy.val
        #     res = max(s, res)
        #     cur = cur.next
        # return res
        if not head:
            return
        values = []
        while head:
            values.append(head.val)
            head = head.next
        n = len(values)
        max_sum = 0
        for i in range(n // 2):
            twin_sum = values[i] + values[n-1-i]
            max_sum = max(twin_sum, max_sum)
        
        return max_sum

        