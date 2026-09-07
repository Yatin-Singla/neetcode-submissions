class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n
        nums.extend(nums[:n-k])
        for i in range(n):
            nums[i] = nums[i+n-k]

        for _ in range(n-k):
            nums.pop()