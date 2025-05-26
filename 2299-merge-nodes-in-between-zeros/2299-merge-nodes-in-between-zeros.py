class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        cur = head
        curD=dummy
        s = 0
        while cur:
            if cur.val != 0:
                s += cur.val
            else:
                if s>0:
                    newN = ListNode(s)
                    curD.next = newN
                    curD = newN
                s = 0
            cur = cur.next
    
        return dummy.next