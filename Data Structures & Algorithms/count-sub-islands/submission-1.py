class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        # traverse grid 2 island
        # iterate over visited from each island in grid2 over grid 1 to check sub island condition
        m, n = len(grid1), len(grid1[0])
        visited = set()
        dirs = [(0,1), (0,-1), (1,0), (-1,0)]
        subIslands = 0

        def inBounds(x,y):
            return 0 <= x < m and 0 <= y < n

        def dfs(x,y):
            queue = deque([(x,y)])
            while queue:
                x,y = queue.popleft()
                for dx, dy in dirs:
                    X, Y = x+dx, y+dy
                    if (X,Y) not in island and inBounds(X,Y) and grid2[X][Y] == 1:
                        island.add((X,Y))
                        queue.append((X,Y))
            return

        for i in range(m):
            for j in range(n):
                if grid2[i][j] == 1 and (i, j) not in visited:
                    island = set([(i,j)])
                    dfs(i,j)
                
                    isSubIsland = True
                    for x,y in island:
                        if grid1[x][y] != 1:
                            isSubIsland = False
                            break

                    subIslands += int(isSubIsland)
                    visited.update(island)


        return subIslands
