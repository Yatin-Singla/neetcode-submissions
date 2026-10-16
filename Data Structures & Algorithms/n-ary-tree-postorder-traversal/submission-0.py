"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        output = []
  
        if not root:
            return output
        
        def helper(node):
            
            for child in node.children:
                helper(child)
            
            output.append(node.val)
            
            return 
        
        helper(root)
        return output