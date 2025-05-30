# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder:
            return None
        root = TreeNode(preorder[0])
        stack = [root]
        inIndex = 0
        for i in range(1, len(preorder)):
            node = TreeNode(preorder[i])
           

            if stack[-1].val != inorder[inIndex]:
                stack[-1].left = node
            else:
                while stack and stack[-1].val == inorder[inIndex]:
                    top = stack.pop()
                    inIndex += 1
                top.right = node
            stack.append(node)
        return root
