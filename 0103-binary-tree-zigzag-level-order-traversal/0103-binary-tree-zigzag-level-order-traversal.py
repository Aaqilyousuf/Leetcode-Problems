# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        queue = deque([root])
        res = []
        count = 1
        while queue:
            lev = []
            for i in range(len(queue)):
                node = queue.popleft()
                lev.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            if count%2!=0:
                res.append(lev)
            else:
                res.append(lev[::-1])
            count+=1
        return res