# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        val = []
        stack = []
        while stack or root:
            while root:
                stack.append(root)
                
                root = root.left
            root = stack.pop()
            val.append(root.val)
            root = root.right
        hashMap = {}
        for i, num in enumerate(val):
            comp = k - num
            if comp in hashMap:
                return True
            hashMap[num] = i
        return False