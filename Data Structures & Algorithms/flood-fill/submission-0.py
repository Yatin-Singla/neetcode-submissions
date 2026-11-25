class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        m, n = len(image), len(image[0])
        originalColor = image[sr][sc]
        dirs = [(0,1),(0,-1),(1,0),(-1,0)]
        visited = set()

        def inBounds(i, j):
            return 0 <= i < m and 0 <= j < n

        def dfs(i, j):
            image[i][j] = color
            visited.add((i,j))

            for dx, dy in dirs:
                x, y = i + dx, j + dy
                if inBounds(x,y) and (x,y) not in visited and image[x][y] == originalColor:
                    dfs(x, y)
        
        dfs(sr, sc)
        return image

            