# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        list_val = []
        while head:
            list_val.append(head.val)
            head=head.next
        l = 0
        r = len(list_val)-1
        while l < r:
            if list_val[l] != list_val[r]:
                return False
            l+=1
            r-=1
        return True