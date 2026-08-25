# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # given a tree
        # root is at 0 of preorder
        # find root in -> inorder
        #   all elements on left root in inorder make up left subtree
        #   all elements on right of root in inorder make up right subtree
        #   adjust bounds accordingly
        n = len(preorder)
        idx_map = {val: i for i, val in enumerate(inorder)}
        def construct(preLow, preHigh, inLow, inHigh):
            # base case
            if preLow > preHigh or inLow > inHigh:
                return None
            
            root_val = preorder[preLow]
            node = TreeNode(val=root_val)
            mid = idx_map[root_val]
            leftSubTreeCount = mid - inLow
            
            node.left = construct(preLow+1, preLow + leftSubTreeCount, inLow, mid - 1)
            node.right = construct(preLow + leftSubTreeCount + 1, preHigh, mid + 1, inHigh)

            return node
        
        return construct(0, n-1, 0, n-1)