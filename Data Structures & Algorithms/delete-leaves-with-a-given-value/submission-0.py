# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        def postOrder(root):
            if not root:
                return True
            
            left = postOrder(root.left)
            right = postOrder(root.right)

            if left:
                root.left = None
            if right:
                root.right = None

            return left and right and root.val == target
        
        if postOrder(root):
            return None

        return root