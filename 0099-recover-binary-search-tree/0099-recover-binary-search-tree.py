# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        # if root.left and root.left.val > root.val:
        #     temp = root.left.val
        #     root.left.val = root.val
        #     root.val = temp
        # if root.right and root.right.val < root.val:
        #     temp1 = root.right.val
        #     root.right.val = root.val
        #     root.val = temp1
        stack = []
        first = second = prev = None
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            if prev and prev.val > root.val:
                if not first:
                    first = prev
                    second = root
                else:
                    second = root
            prev = root
            root = root.right
        if first and second:
            first.val, second.val = second.val, first.val
            

        