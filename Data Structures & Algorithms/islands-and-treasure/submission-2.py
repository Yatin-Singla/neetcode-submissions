class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        def inBounds(x,y):
            return 0 <= x < m and 0 <= y < n

        m, n = len(grid), len(grid[0])
        dirs = [(0,1),(0,-1),(1,0),(-1,0)]
        dist, queue = 0, deque()
        
        for row in range(m):
            for col in range(n):
                if grid[row][col] == 0:
                    queue.append((row, col))
  
        while queue:
            size = len(queue)
            for _ in range(size):
                x, y = queue.popleft()
                for dx, dy in dirs:
                    if inBounds(x+dx, y+dy) and grid[x+dx][y+dy] == (2**31 - 1):
                        # Mark it IMMEDIATELY so no other node enqueues it again
                        grid[x+dx][y+dy] = dist + 1
                        queue.append((x+dx, y+dy))

            dist += 1

        return