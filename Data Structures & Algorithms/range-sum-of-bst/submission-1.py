# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        if not root:
            return 0
        
        # If current node's value is less than low, 
        # skip the left subtree and go right.
        if root.val < low:
            return self.rangeSumBST(root.right, low, high)
        
        # If current node's value is greater than high,
        # skip the right subtree and go left.
        if root.val > high:
            return self.rangeSumBST(root.left, low, high)
        
        # Otherwise, the current node is in the range.
        # Add its value and check both subtrees.
        return (root.val + 
                self.rangeSumBST(root.left, low, high) + 
                self.rangeSumBST(root.right, low, high))
