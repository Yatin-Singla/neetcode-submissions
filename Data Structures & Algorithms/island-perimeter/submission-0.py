class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        def inBounds(row, col):
            return 0 <= row < m and 0 <= col < n
            
        def dfs(row, col):
            if not inBounds(row, col):
                return 1
            if grid[row][col] == 0:
                return 1
            if (row, col) in visited:
                return 0

            visited.add((row, col))
            boundary = 0
            for dx, dy in dirs:
                boundary += dfs(row+dx, col+dy)

            return boundary

        m, n = len(grid), len(grid[0])
        dirs = [(0,1), (0,-1), (1,0), (-1,0)]
        visited = set()
        perimeter = 0
        for row in range(m):
            for col in range(n):
                perimeter = max(perimeter, dfs(row, col))

        return perimeter