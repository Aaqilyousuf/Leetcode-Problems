# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        queue = deque([(root, 0)])
        maxWidth = 0
        while queue:
            levlen = len(queue)
            _, firstInd = queue[0]
            _, lastInd = queue[-1]
            maxWidth = max(maxWidth, lastInd-firstInd+1)
            for i in range(len(queue)):
                node, index = queue.popleft()
                if node.left:
                    queue.append((node.left, 2*index+1))
                if node.right:
                    queue.append((node.right, 2*index+2))
            
        return maxWidth