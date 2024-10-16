# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        stack = []
        count= 0
        cur = root
        while cur or stack:
            while cur:
                count+=1
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            cur = cur.right
        return count