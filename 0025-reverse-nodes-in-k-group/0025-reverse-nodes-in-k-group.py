class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head, k):
        prev = None
        cur = head
        for _ in range(k):
            nextNode = cur.next
            cur.next = prev
            prev = cur
            cur = nextNode
        return prev, cur

    def reverseKGroup(self, head, k):
        dummy = ListNode(0)
        dummy.next = head
        ptr = dummy
        while ptr:
            temp = ptr
            for _ in range(k):
                temp = temp.next
                if not temp:
                    return dummy.next
            prev, cur = self.reverseList(ptr.next, k)

            lastNode_of_reversed = ptr.next #it still store the old node (before revesed node for ex in the second example the ptr.next is node(1))
            lastNode_of_reversed.next = cur #(lets take ex2 here cur is node(4)) so we connected our nodes
            ptr.next = prev

            ptr = lastNode_of_reversed #now moving for next revese
        return dummy.next


        
        