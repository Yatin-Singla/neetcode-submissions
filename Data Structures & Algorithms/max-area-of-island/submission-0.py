class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def inBounds(x, y):
            return 0 <= x < m and 0 <= y < n
        
        def iterativeDFS(x, y):
            if grid[x][y] == 0:
                return 0
            
            area = 0
            grid[x][y] = 0
            stack = [(x,y)]

            while stack:
                x, y = stack.pop()
                area += 1
                for dx, dy in dirs:
                    if inBounds(x+dx, y+dy) and grid[x+dx][y+dy] == 1:
                        grid[x+dx][y+dy] = 0
                        stack.append((x+dx, y+dy))

            return area

        maxArea = 0
        m, n = len(grid), len(grid[0])
        dirs = [(0,1),(0,-1),(1,0),(-1,0)]

        for row in range(m):
            for col in range(n):
                area = iterativeDFS(row, col)
                maxArea = max(maxArea, area)
                
        return maxArea