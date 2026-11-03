# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from math import inf

class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        vals = []
        
        def inorder(node):
            if not node:
                return

            inorder(node.left)
            vals.append(node.val)
            inorder(node.right)


        inorder(root)
        minDiff = inf
        for i in range(1, len(vals)):
            minDiff = min(minDiff, vals[i] - vals[i-1])

        return minDiff