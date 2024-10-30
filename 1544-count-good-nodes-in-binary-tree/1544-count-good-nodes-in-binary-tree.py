# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, max_val):
            if not node:
                return 0
            # Check if the current node is a good node
            good_node_count = 1 if node.val >= max_val else 0
            # Update the maximum value seen so far
            max_val = max(max_val, node.val)
            # Recursively count good nodes in the left and right subtrees
            good_node_count += dfs(node.left, max_val)
            good_node_count += dfs(node.right, max_val)
            return good_node_count
        
        return dfs(root, root.val)  # Start with the root value as the initial max
