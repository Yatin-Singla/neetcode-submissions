class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        pos = 0
        while nums[pos] > 0:
            tmp = nums[pos]
            nums[pos] = -tmp
            pos = tmp

        return pos