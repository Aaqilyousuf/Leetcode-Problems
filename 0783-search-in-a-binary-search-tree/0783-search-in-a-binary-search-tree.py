# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        stack = []
        cur = root
        dummy = None
        while cur or stack:
            while cur:
                if cur.val == val:
                    dummy = cur
                    dummy.left = cur.left
                    dummy.right = cur.right
                    
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            cur = cur.right
        return dummy
