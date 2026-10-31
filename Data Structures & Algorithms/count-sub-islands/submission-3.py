class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        # remove all non subislands then count all remaining subIslands
        m, n = len(grid1), len(grid1[0])
        dirs = [(0,1), (0,-1), (1,0), (-1,0)]
        
        def inBounds(i, j):
            return 0 <= i < m and 0 <= j < n

        def traverse(i, j):
            queue = deque([(i,j)])
            while queue:
                i, j = queue.popleft()
                for dx, dy in dirs:
                    newX, newY = i+dx, j+dy
                    if inBounds(newX,newY) and grid2[newX][newY] == 1:
                        grid2[newX][newY] = 0
                        queue.append((newX, newY))
        
        for i in range(m):
            for j in range(n):
                if grid2[i][j] == 1 and grid1[i][j] == 0:
                    # remove islands from grid2
                    grid2[i][j] = 0
                    traverse(i, j)

        subIslandCount = 0
        for i in range(m):
            for j in range(n):
                if grid2[i][j] == 1:
                    grid2[i][j] = 0
                    traverse(i, j)
                    subIslandCount += 1

        return subIslandCount
        