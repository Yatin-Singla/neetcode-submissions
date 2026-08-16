from functools import lru_cache
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        @lru_cache()
        def countPaths(x,y):
            if x == m-1 and y == n-1:
                return 1
            if x == m or y == n:
                return 0
            
            return countPaths(x+1, y) + countPaths(x, y+1)
        return countPaths(0,0)