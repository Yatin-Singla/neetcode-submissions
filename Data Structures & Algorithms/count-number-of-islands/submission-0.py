class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def inBounds(x, y):
            return 0 <= x < m and 0 <= y < n

        def dfs(x, y):
            if inBounds(x,y) and int(grid[x][y]):
                grid[x][y] = 0
                dfs(x+1, y)
                dfs(x-1, y)
                dfs(x, y+1)
                dfs(x, y-1)

        m, n = len(grid), len(grid[0])
        islandCount = 0
        for row in range(m):
            for col in range(n):
                if int(grid[row][col]):
                    islandCount += 1
                    dfs(row, col)

        return islandCount