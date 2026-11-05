# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        def traversal(nodeA, nodeB):
            if not nodeA and not nodeB:
                return True
            if not nodeA or not nodeB:
                return False

            if nodeA.val != nodeB.val:
                return False
            
            return traversal(nodeA.left, nodeB.right) and traversal(nodeA.right, nodeB.left)

        return traversal(root.left, root.right)