class Solution:
    def climbStairs(self, n: int) -> int:
        # Approach 0.5 - Brute Force
        # Approach 1 - Top Down Memoization
        # approach 2 - Bottom up Tabulation
        # Approach 3 - Optimized Tabulation
        if n < 2:
            return 1
        prev, lag = 1, 1
        curr = 0
        for i in range(2, n+1):
            curr = prev + lag
            lag, prev = prev, curr

        return curr
