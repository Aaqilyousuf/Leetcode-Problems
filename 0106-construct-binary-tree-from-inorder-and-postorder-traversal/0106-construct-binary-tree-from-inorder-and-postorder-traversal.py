# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not inorder or not postorder:
            return None
        rootVal = postorder[-1]
        root = TreeNode(rootVal)
        mid = inorder.index(rootVal)
        leftSub = mid
        root.left = self.buildTree(inorder[:mid], postorder[:leftSub]) 
        root.right = self.buildTree(inorder[mid+1:], postorder[leftSub:-1])

        return root