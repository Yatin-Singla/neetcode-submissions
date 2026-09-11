# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        inorder = []

        def inOrder(root):
            if not root:
                return
            
            inOrder(root.left)
            if root.val != key:
                inorder.append(root)
            inOrder(root.right)

        def construct(left, right):
            if right < left:
                return
            mid = (left + right) >> 1
            inorder[mid].left = construct(left, mid - 1)
            inorder[mid].right = construct(mid + 1, right)

            return inorder[mid]

        inOrder(root)

        return construct(0, len(inorder)-1)