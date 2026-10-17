class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        maxFishCollected = 0
        visited = set()

        def dfs(x,y):
            if not (0 <= x < n and 0 <= y < m):
                return 0 
            if grid[x][y] == 0 or (x,y) in visited:
                return 0

            visited.add((x,y))
            fishCollected = grid[x][y]
            for dx, dy in dirs:
                X, Y = x+dx, y+dy
                fishCollected += dfs(X, Y)    

            return fishCollected

        n, m = len(grid), len(grid[0])
        dirs = [(0,1), (0,-1), (1,0), (-1,0)]
        for i in range(n):
            for j in range(m):
                maxFishCollected = max(dfs(i, j), maxFishCollected)

        return maxFishCollected
