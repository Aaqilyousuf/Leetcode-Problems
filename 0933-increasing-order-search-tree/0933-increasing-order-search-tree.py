# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        stack = []
        dummy = cur = TreeNode()

        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            cur.right = root

            cur = cur.right
            root = root.right
            cur.left = None
        return dummy.right