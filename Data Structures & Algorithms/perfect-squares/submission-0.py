from functools import lru_cache
from math import inf
class Solution:
    def numSquares(self, n: int) -> int:
        options = [i for i in range(int(n**0.5) + 1, 0, -1)]

        @lru_cache(maxsize=None)
        def dfs(currSum):
            if currSum > n:
                return inf
            elif currSum == n:
                return 0

            selected = inf
            for i in range(len(options)):
                selected = min(selected, 1 + dfs(currSum + (options[i]**2)))

            return selected

        return dfs(0)