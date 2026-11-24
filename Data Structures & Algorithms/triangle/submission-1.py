class Solution:
    def minimumTotal(self, triangle: list[list[int]]) -> int:
        m = len(triangle)
        for row in range(1, m):
            triangle[row][0] += triangle[row-1][0]
            for col in range(1, len(triangle[row])-1):
                triangle[row][col] += min(triangle[row-1][col], triangle[row-1][col-1])

            triangle[row][-1] += triangle[row-1][-1]

        return min(triangle[-1])