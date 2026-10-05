class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        def helper(r, c, size):
            if size == 1:
                return Node(grid[r][c] == 1, True, None, None, None, None)

            half = size >> 1
            tl = helper(r, c, half)
            tr = helper(r, c + half, half)
            bl = helper(r + half, c, half)
            br = helper(r + half, c + half, half)

            if (tl.isLeaf and tr.isLeaf and bl.isLeaf and br.isLeaf
                    and tl.val == tr.val == bl.val == br.val):
                return Node(tl.val, True, None, None, None, None)

            return Node(True, False, tl, tr, bl, br)

        return helper(0, 0, len(grid))