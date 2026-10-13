from functools import lru_cache
from math import inf
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        #change(amt) = min coins needed that sum to amount
        #change(amt) = 1 + change(amt - coinI)
        @lru_cache(maxsize=None)
        def change(amt):
            if amt == 0:
                return 0

            res = inf

            for coin in coins:
                if amt - coin >= 0:
                    res = min(res, 1 + change(amt - coin))

            return res
        
        coinsNeeded = change(amount)
        return coinsNeeded if coinsNeeded != inf else -1