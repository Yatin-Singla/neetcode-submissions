from math import inf
from functools import lru_cache
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        @lru_cache(maxsize=None)
        def helper(idx, prev):
            if idx == len(nums):
                return 0
            
            inclusive = 0
            
            if nums[idx] > prev:
                inclusive += 1 + helper(idx+1, nums[idx])

            return max(helper(idx+1, prev), inclusive)
        
        return helper(0, -inf)