"""
nums =      [1,  2, 4,6]
forward =   [1,  2, 8,24]
backward =  [48,48,24,6]
"""

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        answer = [1]*n
        
        # LEFT PRODUCT         
        for i in range(1,n):
            answer[i] = answer[i-1]*nums[i-1]
        
        # KEEP RUNNING PRODUCT IN A VARIABLE
        runningRightProduct = nums[-1]
        for i in range(n-2, -1, -1):
            answer[i] = answer[i]*runningRightProduct
            runningRightProduct *= nums[i]
        
        return answer