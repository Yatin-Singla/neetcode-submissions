class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        start, end = 1, 1
        while end < len(nums):
            if nums[end] != nums[end - 1]:
                nums[start] = nums[end]
                start += 1
            end += 1
                
        return start