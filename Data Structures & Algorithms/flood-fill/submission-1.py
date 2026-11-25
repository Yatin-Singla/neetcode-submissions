class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        m, n = len(image), len(image[0])
        originalColor = image[sr][sc]
        dirs = [(0,1),(0,-1),(1,0),(-1,0)]

        def inBounds(i, j):
            return 0 <= i < m and 0 <= j < n

        def dfs(i, j):
            if not inBounds(i,j) or image[i][j] != originalColor:
                return
            if image[i][j] == color:
                return

            image[i][j] = color

            for dx, dy in dirs:
                dfs(i + dx, j + dy)
        
        dfs(sr, sc)
        return image

            