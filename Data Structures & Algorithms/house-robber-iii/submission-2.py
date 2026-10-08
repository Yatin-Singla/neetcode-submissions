# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from functools import lru_cache
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        @lru_cache()
        def postOrder(node):
            if not node:
                return 0

            res = node.val
            if node.left:
                res += postOrder(node.left.left) + postOrder(node.left.right)
            if node.right:
                res += postOrder(node.right.left) + postOrder(node.right.right)
            
            return max(res, postOrder(node.left) + postOrder(node.right))
        
        return postOrder(root)