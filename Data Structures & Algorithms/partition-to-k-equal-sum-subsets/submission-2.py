class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        if sum(nums) % k != 0: return False

        nums.sort(reverse=True)
        targetSum = sum(nums) / k
        used = [False]*len(nums)

        def backtrack(idx, partition, subsetSum):
            if partition == 0:
                return True
            if subsetSum == targetSum:
                return backtrack(0, partition-1, 0)
            
            for j in range(idx, len(nums)):
                if used[j] or subsetSum + nums[j] > targetSum:
                    continue
                used[j] = True
                if backtrack(j+1, partition, subsetSum + nums[j]):
                    return True
                used[j] = False

            return False

        return backtrack(0, k, 0)
        