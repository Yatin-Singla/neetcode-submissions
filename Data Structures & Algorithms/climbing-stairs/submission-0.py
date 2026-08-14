from functools import lru_cache
class Solution:
    @lru_cache()
    def climbStairs(self, n: int) -> int:
        # Approach 0.5 - Brute Force
        # Approach 1 - Top Down Memoization
        # approach 2 - Bottom up Tabulation
        # Approach 3 - Optimized Tabulation
        if n <= 1:
            return 1
        return self.climbStairs(n-1) + self.climbStairs(n-2)