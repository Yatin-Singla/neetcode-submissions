from math import inf
from collections import defaultdict
class Solution:
    def numSquares(self, n: int) -> int:
        options = [i for i in range(1, int(n**0.5) + 1)]
        memo = defaultdict(lambda: inf)
        memo[n] = 0

        for currSum in range(n, 0, -1):
            if memo[currSum] == inf:
                continue
            for option in options:
                if option**2 > currSum:
                    break

                memo[currSum - (option**2)] = min(1 + memo[currSum], memo[currSum - (option**2)])

        return memo[0]