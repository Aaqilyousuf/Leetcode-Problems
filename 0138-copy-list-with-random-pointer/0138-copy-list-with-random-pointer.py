class Node:
    def __init__(self, val=0, next=None, random=None):
        self.val = val
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return None
        
        head = self.connectBw(head)
        self.connectRandom(head)
        return self.deepCopy(head)

    def connectBw(self, head: 'Node') -> 'Node':
        temp = head
        while temp:
            copyNode = Node(temp.val)
            copyNode.next = temp.next
            temp.next = copyNode
            temp = temp.next.next
        return head

    def connectRandom(self, head: 'Node'):
        temp = head
        while temp:
            copyNode = temp.next
            if temp.random:
                copyNode.random = temp.random.next
            else:
                copyNode.random = None
            temp = temp.next.next

    def deepCopy(self, head: 'Node') -> 'Node':
        # Separate the copied list from the original list
        dummyNode = Node(-1)
        res = dummyNode
        temp = head
        while temp:
            # Connect the copied list to the dummy node
            res.next = temp.next
            temp.next = temp.next.next
            # Move to the next connection
            res = res.next
            temp = temp.next
        return dummyNode.next
