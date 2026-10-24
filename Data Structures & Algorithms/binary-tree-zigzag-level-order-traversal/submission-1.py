# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        output = []
        queue = deque([root])

        while queue:
            size = len(queue)
            output.append([])
            for _ in range(size):
                node = queue.popleft()
                output[-1].append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        
        for i in range(1, len(output), 2):
            output[i] = output[i][::-1]

        return output
