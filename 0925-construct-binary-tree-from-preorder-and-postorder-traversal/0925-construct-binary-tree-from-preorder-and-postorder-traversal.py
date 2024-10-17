# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not postorder:
            return None
        root = TreeNode(preorder[0])
        
        if len(preorder) == 1:
            return root
        leftSub_Tree = preorder[1]
        leftSub_Size = postorder.index(leftSub_Tree) + 1
        root.left = self.constructFromPrePost(preorder[1: leftSub_Size + 1], postorder[:leftSub_Size])
        root.right = self.constructFromPrePost(preorder[leftSub_Size + 1:], postorder[leftSub_Size:-1])
        return root