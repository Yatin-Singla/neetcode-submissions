class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        rowBelow, colAhead = [0]*n, 1
        rowBelow[-1] = 1
        for row in range(m-1, -1, -1):
            for col in range(n-1, -1, -1):
                if row == m-1 and col == n-1:
                    continue
                rowBelow[col] = rowBelow[col] + colAhead
                colAhead = rowBelow[col]
            colAhead = 0

        return rowBelow[0]