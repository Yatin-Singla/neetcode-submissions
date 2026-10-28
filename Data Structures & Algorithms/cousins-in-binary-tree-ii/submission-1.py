# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        queue = deque([(TreeNode(-1), root)])
        parentSum = defaultdict(int)
        while queue:
            size = len(queue)
            lvlSum = 0
            for parent, node in queue:
                parentSum[parent] += node.val
                lvlSum += node.val
            for _ in range(size):
                parent, node = queue.popleft()
                node.val = lvlSum - parentSum[parent]
                if node.left:
                    queue.append((node, node.left))
                if node.right:
                    queue.append((node, node.right))

        return root            
