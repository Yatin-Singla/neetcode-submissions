class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        output = []
        option = deque(["a", "b", "c"])
        
        def happyString(curr):
            if len(curr) == n:
                output.append(''.join(curr))
                return

            for ch in option:
                if curr and curr[-1] != ch:
                    curr.append(ch)
                    happyString(curr)
                    curr.pop()
                elif not curr:
                    curr.append(ch)
                    happyString(curr)
                    curr.pop()

        happyString([])

        return output[k-1] if len(output) >= k else ""
