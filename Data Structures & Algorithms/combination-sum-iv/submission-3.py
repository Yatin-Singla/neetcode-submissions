from functools import lru_cache
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        nums.sort()
        dp = defaultdict(int)
        dp[target] = 1

        for currSum in range(target, 0, -1):
            for num in nums:
                if currSum < num:
                    break
                dp[currSum - num] += dp[currSum]

        return dp[0]