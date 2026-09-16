from functools import reduce
class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        sumXOR = 0

        def XORTotal(nums):
            if not nums:
                return 0
            
            return reduce(lambda x, y: x^y, nums)

        def subset(curr, idx):
            nonlocal sumXOR
            if idx >= len(nums):
                sumXOR += XORTotal(curr)
                return
            subset(curr, idx + 1)
            curr.append(nums[idx])
            subset(curr, idx + 1)
            curr.pop()

        subset([], 0)
        return sumXOR