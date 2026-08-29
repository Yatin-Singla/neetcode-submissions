class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        candidate, frequency = nums[0], 1
        for i in range(1, len(nums)):
            if frequency == 0:
                candidate = nums[i]
            if nums[i] == candidate:
                frequency += 1
            else:
                frequency -= 1

        return candidate