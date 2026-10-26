class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        currComb, output = [], []
        nums.sort()

        def combinations(i):
            if i == len(nums):
                output.append(currComb[:])
                return

            combinations(i+1)
            currComb.append(nums[i])
            combinations(i+1)
            currComb.pop()
        
        combinations(0)
        return output