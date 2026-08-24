class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m, n = len(matrix), len(matrix[0])
        dirs = [(0,1),(1,0), (0,-1),(-1,0)]
        seen = set()
        output = []

        def inBounds(i, j):
            return 0 <= i < m and 0 <= j < n
        def dfs(i, j, idx):
            seen.add((i,j))
            output.append(matrix[i][j])
            counter = 0
            while counter < 4:
                dx, dy = dirs[idx]
                x = i + dx
                y = j + dy
                if inBounds(x,y) and (x,y) not in seen:
                    dfs(x,y, idx)
                else:
                    idx = (idx + 1) % 4

                counter += 1

        dfs(0,0,0)
        return output