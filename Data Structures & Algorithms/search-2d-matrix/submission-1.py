class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        low, high = 0, m*n -1
        while low <= high:
            mid = (low + high) >> 1
            mRow = mid // n
            mCol = mid % n
            if target == matrix[mRow][mCol]:
                return True
            elif target > matrix[mRow][mCol]:
                low = mid + 1
            else:
                high = mid - 1

        return False