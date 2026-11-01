class Solution:
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        isSubList = False
        
        def traverse(treeNode, listNode):
            nonlocal isSubList
            if isSubList:
                return
            # leaf check
            if not listNode:
                isSubList = True
                return
            # base case
            if not treeNode:
                return

            if treeNode.val == listNode.val:
                return traverse(treeNode.left, listNode.next) or \
                traverse(treeNode.right, listNode.next)
            else:
                if listNode != head:
                    return
                return traverse(treeNode.left, listNode) or \
                traverse(treeNode.right, listNode)

        traverse(root, head)
        return isSubList
            

            
