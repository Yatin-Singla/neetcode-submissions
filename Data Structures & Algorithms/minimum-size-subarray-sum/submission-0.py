from math import inf
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        minLength = inf
        subArraySum = [0]
        for num in nums:
            subArraySum.append(subArraySum[-1] + num)

        left = right = 0
        while right < len(subArraySum):
            while subArraySum[right] - subArraySum[left] >= target:
                minLength = min(minLength, right - left)
                left += 1
                
            right += 1

        return minLength if minLength is not inf else 0