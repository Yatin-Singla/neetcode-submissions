class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        sumTotal = 0
        def subset(idx, total):
            nonlocal sumTotal
            if idx >= len(nums):
                sumTotal += total
                return 

            subset(idx + 1, total)
            subset(idx + 1, total^nums[idx])

        subset(0, 0)
        return sumTotal
