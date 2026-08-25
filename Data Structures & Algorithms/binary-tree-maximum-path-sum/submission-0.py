# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        pathSum = root.val
        def postOrder(node):
            nonlocal pathSum
            if not node:
                return 0
            
            leftSum = postOrder(node.left)
            rightSum = postOrder(node.right)

            pathSum = max(pathSum, leftSum + rightSum + node.val, \
            leftSum + node.val, rightSum + node.val, node.val)

            # both left sum and right sum can be negative
            return max(leftSum + node.val, rightSum + node.val, node.val)
        
        postOrder(root)
        return pathSum
        