"""
nums =      [1,  2, 4,6]
forward =   [1,  2, 8,24]
backward =  [48,48,24,6]
"""

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        forward, backward = [nums[0]]*n, [nums[-1]]*n

        for i in range(1, n):
            forward[i] = forward[i-1]*nums[i]
            backward[n-i-1] = backward[n-i]*nums[n-i-1]

        output = [backward[1]]*n
        output[-1] = forward[n-2]

        for i in range(1,n-1):
            output[i] = forward[i-1]*backward[i+1]

        return output