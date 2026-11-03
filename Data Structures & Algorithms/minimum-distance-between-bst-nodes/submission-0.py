# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from math import inf

class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        minDiff = inf
        def preOrder(node, maxVal = inf, minVal = -inf):
            nonlocal minDiff
            if not node:
                return
            
            minDiff = min(minDiff, maxVal - node.val, node.val - minVal)
            if node.left:
                minDiff = min(minDiff, node.val - node.left.val)
                preOrder(node.left, node.val, minVal)
            if node.right:
                minDiff = min(minDiff, node.right.val - node.val)
                preOrder(node.right, maxVal, node.val)

        preOrder(root)
        return minDiff