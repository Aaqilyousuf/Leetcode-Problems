# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        def findMin(node):
            while node.left:
                node = node.left
            return node

        parent = None
        curr = root

        #Find the node to delete
        while curr and curr.val != key:
            parent = curr
            if key < curr.val:
                curr = curr.left
            else:
                curr = curr.right

        if not curr:
            return root  #Key not found

        def deleteNodeHelper(node):
            if not node.left:
                return node.right
            if not node.right:
                return node.left
            minNode = findMin(node.right)
            node.val = minNode.val
            node.right = self.deleteNode(node.right, minNode.val)
            return node

        #Delete the node
        if not parent:
            return deleteNodeHelper(curr)  

        if parent.left == curr:
            parent.left = deleteNodeHelper(curr)
        else:
            parent.right = deleteNodeHelper(curr)

        return root
