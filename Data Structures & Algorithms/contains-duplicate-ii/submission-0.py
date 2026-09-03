class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        seen = set()
        i = 0
        for j in range(len(nums)):
            if nums[j] in seen:
                return True
            seen.add(nums[j])
            if len(seen) > k:
                seen.discard(nums[i])
                i += 1

        return False
            
