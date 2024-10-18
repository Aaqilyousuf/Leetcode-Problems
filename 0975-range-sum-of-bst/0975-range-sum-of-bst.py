# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        stack = []
        cur = root
        sum = 0
        while cur or stack:
            while cur:
                if low<=cur.val<=high:
                    sum += cur.val
                stack.append(cur)
                cur = cur.left 
            cur = stack.pop()
            cur = cur.right
        return sum