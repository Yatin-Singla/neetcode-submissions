class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k %= n
        count = start = 0

        while count < n:
            prev = nums[start]
            current = start
            while True:
                nIdx = (current + k) % n
                nums[nIdx], prev = prev, nums[nIdx]
                current = nIdx
                count += 1

                if current == start:
                    break
            start += 1

        