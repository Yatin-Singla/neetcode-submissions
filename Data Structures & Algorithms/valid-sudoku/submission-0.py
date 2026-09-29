class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        unique = set()
        offset = [(0,0), (0,3), (0,6), (3,0), (3,3), (3,6), (6,0), (6,3), (6,6)]
        # col check
        for col in range(9):
            unique.clear()
            for row in range(9):
                if board[row][col] in unique:
                    return False
                if board[row][col] != ".":
                    unique.add(board[row][col])

        # row check
        for row in range(9):
            unique.clear()
            for col in range(9):
                if board[row][col] in unique:
                    return False
                if board[row][col] != ".":
                    unique.add(board[row][col])

        # grid check
        for x, y in offset:
            unique.clear()
            for dx in range(3):
                for dy in range(3):
                    if board[x+dx][y+dy] in unique:
                        return False
                    if board[x+dx][y+dy] != ".":
                        unique.add(board[x+dx][y+dy])

        return True




