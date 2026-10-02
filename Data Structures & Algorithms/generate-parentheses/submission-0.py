class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        output = []
        def backtrack(curr, openCount, closedCount):
            if openCount < 0:
                return
            if closedCount < openCount:
                return
            if len(curr) == 2*n:
                output.append("".join(curr))
                return
            
            curr.append("(")
            backtrack(curr, openCount - 1, closedCount)
            curr[-1] = ")"
            backtrack(curr, openCount, closedCount - 1)
            curr.pop()

        backtrack([], n, n)
        return output