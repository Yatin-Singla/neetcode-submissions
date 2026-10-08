class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 2:
            return max(nums)
        def loot(houses):
            if not houses:
                return 0
            next, head = houses[-1], 0
            for i in range(len(houses)-2, -1, -1):
                curr = max(houses[i] + head, next)
                head, next = next, curr

            return max(next, head)
        
        return max(nums[0] + loot(nums[2:n-1]), loot(nums[1:]))
