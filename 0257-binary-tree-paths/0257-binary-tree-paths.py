# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        if not root:
            return []
        stack = [(root, str(root.val))]
        ans = []
        while stack:
            node, path = stack.pop()
            if node.right == None and node.left == None:
                ans.append(path)
                
            if node.right:
                stack.append((node.right, path+"->"+str(node.right.val)))
            if node.left:
                stack.append((node.left, path+"->"+str(node.left.val)))

        return ans
