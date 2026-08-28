# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val)
        def traversal(root):
            if not root:
                return None

            if val < root.val and not root.left:
                root.left = TreeNode(val)
            elif val < root.val:
                traversal(root.left)
            elif val > root.val and not root.right:
                root.right = TreeNode(val)
            elif val > root.val:
                traversal(root.right)

        traversal(root)
        return root