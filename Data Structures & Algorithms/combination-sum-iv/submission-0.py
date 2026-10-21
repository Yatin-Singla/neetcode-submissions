from functools import lru_cache
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        nums.sort()

        @lru_cache(maxsize=None)
        def dfs(currSum):
            if currSum > target:
                return 0
            elif currSum == target:
                return 1

            ans = 0
            for i in range(len(nums)):
                ans += dfs(currSum+nums[i])

            return ans

        return dfs(0)