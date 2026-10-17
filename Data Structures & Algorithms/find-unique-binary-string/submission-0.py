class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        n = len(nums)
        nums = set(nums)

        def backtrack(idx, comb):
            if idx == n:
                ans = "".join(comb)
                if ans not in nums:
                    return ans
                else:
                    return ""

            comb.append("0")
            if ans:=backtrack(idx + 1, comb):
                return ans 
            comb[-1] = "1"
            if ans := backtrack(idx + 1, comb):
                return ans
            comb.pop()

            return ""

        return backtrack(0, [])

