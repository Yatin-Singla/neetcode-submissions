class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # [2,4,-3,5]
        # [1, 2, 8, -24, -120]
        # []
        n = len(nums)
        res, minP, maxP = nums[0],1,1
        
        for i in range(n):
            temp = maxP
            maxP = max(nums[i], temp*nums[i], minP*nums[i])
            minP = min(temp*nums[i], minP*nums[i], nums[i])
            res = max(res, maxP)

        return res

        

        