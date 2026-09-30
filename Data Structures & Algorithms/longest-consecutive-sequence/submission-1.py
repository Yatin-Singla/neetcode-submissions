class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        seqLength = currLen = 1
        prev = min(nums)
        nums = list(set(nums))
        heapq.heapify(nums)
        while nums:
            num = heapq.heappop(nums)
            if num - prev != 1:
                currLen = 1
            elif num - prev == 1:
                currLen += 1
                seqLength = max(seqLength, currLen)
            prev = num

        return seqLength
