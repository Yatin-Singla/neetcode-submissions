from functools import lru_cache
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        nums.sort()
        dp = {0:1}

        for currSum in range(1, target + 1):
            dp[currSum] = 0
            for num in nums:
                dp[currSum] += dp.get(currSum - num, 0)

        return dp[target]