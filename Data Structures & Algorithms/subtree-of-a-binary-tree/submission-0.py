# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        output = False
        if not subRoot:
            return True

        def isSame(p, q):
            if not p and not q: return True
            if not p or not q: return False
            if p.val != q.val: return False
            return isSame(p.left, q.left) and isSame(p.right, q.right)
        
        def traversal(root):
            nonlocal output
            if not root:
                return
            
            if root.val == subRoot.val:
                if isSame(root, subRoot):
                    output = True

            traversal(root.left)
            traversal(root.right)


        traversal(root) 
        return output
