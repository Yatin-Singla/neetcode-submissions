from functools import lru_cache
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        nums.sort()
        
        @lru_cache(maxsize=None)
        def dfs(currSum):
            if currSum > target:
                return 0
            if currSum == target:
                return 1

            combinations = 0
            for num in nums:
                combinations += dfs(currSum + num)

            return combinations

        return dfs(0)
