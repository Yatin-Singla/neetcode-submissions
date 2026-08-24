class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = prefixSum = 0
        lookup = {0:1}

        for i in range(1, len(nums)+1):
            prefixSum = prefixSum + nums[i-1]
            if prefixSum - k in lookup:
                count += lookup[prefixSum - k]
            lookup[prefixSum] = lookup.get(prefixSum, 0) + 1

        return count