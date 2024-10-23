from collections import deque


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        queue = deque([root])
        sumLevel = []
        while queue:
            s = 0
            length = len(queue)
            for _ in range(length):
                node = queue.popleft()
                s += node.val

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            sumLevel.append(s)
        queue = deque([root])
        level = 0
        root.val = 0
        while queue:

            length = len(queue)
            for _ in range(length):
                node = queue.popleft()
                s = 0
                if node.left:
                    s += node.left.val
                if node.right:
                    s += node.right.val
                if node.left:
                    node.left.val = sumLevel[level + 1] - s
                    queue.append(node.left)
                if node.right:
                    node.right.val = sumLevel[level + 1] - s
                    queue.append(node.right)
            level += 1
        return root
