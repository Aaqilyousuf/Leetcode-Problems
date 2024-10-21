from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        
        if not root:
            return None
        queue = deque([root])
        
        res = []
        

        while queue:
           lSum = 0
           lCount = len(queue)

           for _ in range(lCount):
            
                node = queue.popleft()
                lSum += node.val

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
           res.append(lSum / lCount)

        return res
        

        
