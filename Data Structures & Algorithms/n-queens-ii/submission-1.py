class Solution:
    def totalNQueens(self, n: int) -> int:
        output = set()
        def backtracking(row, qLocations):
            if row == n:
                output.add(tuple(qLocations))
                return
            
            for col in range(n):
                isConflict = False
                for x,y in enumerate(qLocations):
                    if row == x or col == y or abs(x-row) == abs(y-col):
                        isConflict = True
                
                if not isConflict:
                    qLocations.append(col)
                    backtracking(row + 1, qLocations)
                    qLocations.pop()
                    
            return
        
        backtracking(0, [])
        return len(output)