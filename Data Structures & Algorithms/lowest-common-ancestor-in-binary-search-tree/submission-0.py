# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        LCA = None
        def postOrder(root):
            nonlocal LCA
            if not root:
                return False

            left = postOrder(root.left)
            right = postOrder(root.right)
            val = root.val == p.val or root.val == q.val
            
            if int(left) + int(right) + int(val) > 1:
                LCA = root

            return left or right or val

        postOrder(root)
        return LCA