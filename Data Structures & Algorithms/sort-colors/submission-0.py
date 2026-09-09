class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        insertIdx = 0
        for end in range(len(nums)):
            if nums[end] == 0:
                nums[insertIdx], nums[end] = nums[end], nums[insertIdx]
                insertIdx += 1

        insertIdx = len(nums) - 1
        for end in range(len(nums)-1, -1, -1):
            if nums[end] == 2:
                nums[insertIdx], nums[end] = nums[end], nums[insertIdx]
                insertIdx -= 1

        return