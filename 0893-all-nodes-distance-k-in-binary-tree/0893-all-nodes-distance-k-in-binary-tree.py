# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        if not root:
            return []
        adjList = defaultdict(list)
        def dfs(node):
            if not node:
                return
            if node.left:
                adjList[node.val].append(node.left.val)
                adjList[node.left.val].append(node.val)
                dfs(node.left)
            if node.right:
                adjList[node.val].append(node.right.val)
                adjList[node.right.val].append(node.val)
                dfs(node.right)
        dfs(root)
        res = []
        visited = set([target.val])
        queue = deque([(target.val, 0)])
        while queue:
            node, no = queue.popleft()
            if no==k:
                res.append(node)
            if no>k:
                break
            for nei in adjList[node]:
                if nei not in visited:
                    visited.add(nei)
                    queue.append((nei, no+1))
        return res
        
            