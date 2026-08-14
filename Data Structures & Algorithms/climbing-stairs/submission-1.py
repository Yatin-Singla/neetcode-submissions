class Solution:
    def climbStairs(self, n: int) -> int:
        # Approach 0.5 - Brute Force
        # Approach 1 - Top Down Memoization
        # approach 2 - Bottom up Tabulation
        # Approach 3 - Optimized Tabulation
        dp = [0]*(n+1)
        dp[0] = dp[1] = 1

        for i in range(2, n+1):
            dp[i] = dp[i-1] + dp[i-2]

        return dp[n]
