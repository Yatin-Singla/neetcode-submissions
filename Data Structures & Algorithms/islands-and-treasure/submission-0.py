class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        def inBounds(x,y):
            return 0 <= x < m and 0 <= y < n

        m, n = len(grid), len(grid[0])
        dirs = [(0,1),(0,-1),(1,0),(-1,0)]
        dist, queue = 0, deque()
        visited = set()
        
        for row in range(m):
            for col in range(n):
                if grid[row][col] == 0:
                    queue.append((row, col))
                    visited.add((row, col))
  
        while queue:
            size = len(queue)
            for _ in range(size):
                x, y = queue.popleft()
                grid[x][y] = dist
                for dx, dy in dirs:
                    if inBounds(x+dx, y+dy) and (x+dx, y+dy) not in visited and grid[x+dx][y+dy] == (2**31 - 1):
                        visited.add((x+dx,y+dy))
                        queue.append((x+dx, y+dy))

            dist += 1

        return