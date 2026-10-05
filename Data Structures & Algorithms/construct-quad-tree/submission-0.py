"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val=False, isLeaf=False, topLeft=None, topRight=None, bottomLeft=None, bottomRight=None):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    # check for all 0s, all 1s, and comb
    def findVal(self, grid, tRow, bRow, lCol, rCol):
        total = 0
        for i in range(tRow, bRow+1):
            for j in range(lCol, rCol+1):
                total += grid[i][j]

        return total

    def construct(self, grid: List[List[int]]) -> 'Node':
        def helper(tRow, bRow, lCol, rCol):
            val = self.findVal(grid, tRow, bRow, lCol, rCol)
            
            # All 0s
            if val == 0:
                return Node(False, True)
            elif val == (bRow - tRow + 1) * (rCol - lCol + 1):
                return Node(True, True)
            # recurse
            else:
                midRow = tRow + bRow >> 1
                midCol = lCol + rCol >> 1
                node = Node(isLeaf = False)
                node.topLeft = helper(tRow, midRow, lCol, midCol)
                node.topRight = helper(tRow, midRow, midCol+1, rCol)
                node.bottomLeft = helper(midRow+1, bRow, lCol, midCol)
                node.bottomRight = helper(midRow+1, bRow, midCol+1, rCol)
                return node
        
        m, n = len(grid), len(grid[0])
        return helper(0, m-1, 0, n-1)
