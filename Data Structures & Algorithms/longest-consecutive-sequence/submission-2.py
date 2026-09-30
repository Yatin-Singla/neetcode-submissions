class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        seqLen = currLen = 1
        nums = list(set(nums))
        nums.sort()
        for i in range(1, len(nums)):
            if nums[i] - nums[i-1] == 1:
                currLen += 1
                seqLen = max(seqLen, currLen)
            else:
                currLen = 1

        return seqLen
