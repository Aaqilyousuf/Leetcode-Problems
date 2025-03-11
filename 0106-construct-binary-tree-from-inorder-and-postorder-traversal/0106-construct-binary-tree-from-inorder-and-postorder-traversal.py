# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        inorder_index = {}
        for ind, val in enumerate(inorder):
            inorder_index[val] = ind
        post_ind = len(postorder) - 1
        def construct(left, right):
            nonlocal post_ind
            if left>right:
                return None
            rootVal = postorder[post_ind]
            post_ind -= 1
            root = TreeNode(rootVal)
            mid = inorder_index[rootVal]

            root.right = construct(mid+1, right)
            root.left = construct(left, mid-1)
            return root
        return construct(0, len(postorder)-1)