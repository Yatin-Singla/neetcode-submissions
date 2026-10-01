class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        seq = set(nums)
        seqLen = 1

        for num in seq:
            if num-1 not in seq:
                currLen = 1
                while num + currLen in seq:
                    currLen += 1
                seqLen = max(currLen, seqLen)

        return seqLen