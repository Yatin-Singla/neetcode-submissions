class Solution:
    def totalNQueens(self, n: int) -> int:
        qPos = set()

        def doesAttack(row, col):
            for x, y in qPos:
                if row == x or col == y:
                    return True
            
            i, j = row, col
            #check diagonal forward
            while i >= 0 and j < n:
                if (i, j) in qPos:
                    return True
                i -= 1
                j += 1

            i, j = row, col
            # check diagonal backward
            while i < n and j >= 0:
                if (i, j) in qPos:
                    return True
                i += 1
                j -= 1

            i, j = row, col
            # check antidiagonal forward
            while i < n and j < n:
                if (i, j) in qPos:
                    return True
                i += 1
                j += 1

            i, j = row, col
            # check antidiagonal backward
            while i >= 0 and j >= 0:
                if (i, j) in qPos:
                    return True
                i -= 1
                j -= 1

            return False

        def backtrack(row):
            if row >= n:
                return 1

            placement = 0
            
            for col in range(n):
                if doesAttack(row, col):
                    continue
                qPos.add((row, col))
                placement += backtrack(row + 1)
                qPos.discard((row, col))

            return placement

        return backtrack(0)