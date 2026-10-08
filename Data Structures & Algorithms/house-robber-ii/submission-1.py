class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)

        def loot(start, stop):
            if start >= stop:
                return 0
            
            prev, behind = nums[start], 0
            for i in range(start+1, stop):
                curr = max(nums[i] + behind, prev)
                behind, prev = prev, curr

            return max(prev, behind)
        
        return max(nums[0] + loot(2, n-1), loot(1, n))
