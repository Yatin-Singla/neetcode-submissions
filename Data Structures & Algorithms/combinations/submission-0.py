class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        output = []
        def backtrack(combination, idx):
            if len(combination) == k:
                output.append(combination[:])
                return
            if idx > n:
                return
            
            backtrack(combination, idx + 1)
            combination.append(idx)
            backtrack(combination, idx + 1)
            combination.pop()

        backtrack([], 1)
        return output