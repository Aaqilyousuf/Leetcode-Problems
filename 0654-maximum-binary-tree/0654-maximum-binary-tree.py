# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        mx = max(nums)
        maxInd = nums.index(mx)
        node = TreeNode(mx)
        if maxInd > 0:
            node.left = self.constructMaximumBinaryTree(nums[:maxInd])
        if maxInd < len(nums)-1:
           node.right = self.constructMaximumBinaryTree(nums[maxInd+1:])
        
        return node
        
            
        