from math import inf
class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        start, diff = 0, inf
        for end in range(k-1, len(nums)):
            diff = min(diff, nums[end]-nums[start])
            if end - start + 1 == k:
                start += 1

        return diff
