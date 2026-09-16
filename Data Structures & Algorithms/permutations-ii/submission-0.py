class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        output = set()
        n = len(nums)
        # set of indices that cannot be used again
        used = set()
        def backtrack(curr):
            if len(curr) >= n:
                output.add(tuple(curr))
                return

            for i in range(n):
                if i not in used:
                    used.add(i)
                    curr.append(nums[i])
                    backtrack(curr)
                    curr.pop()
                    used.discard(i)

        backtrack([])
        return [list(item) for item in output]