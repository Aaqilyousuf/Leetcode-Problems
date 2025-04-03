# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        queue = deque([(root, 0, 0)]) 
        res = []
        verticalDict = defaultdict(list)
        while queue:
            
            node, h1, depth = queue.popleft()
            verticalDict[h1].append((depth, node.val))
            if node.left:
                queue.append((node.left, h1-1, depth+1))
            if node.right:
                queue.append((node.right, h1+1, depth+1))
        for h1 in sorted(verticalDict.keys()):
            columnNode = sorted(verticalDict[h1])
            res.append([val for _, val in columnNode])
        return res
            