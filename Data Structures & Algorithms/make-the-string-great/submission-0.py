class Solution:
    def makeGood(self, s: str) -> str:
        a_ord, A_ord = ord("a"), ord("A")
        stack, squash = [], {} 
        for i in range(26):
            squash[chr(a_ord + i)] = chr(A_ord + i)
            squash[chr(A_ord + i)] = chr(a_ord + i)

        for i, ch in enumerate(s):
            if stack and squash[stack[-1]] == ch:
                stack.pop()
            else:
                stack.append(ch)

        return "".join(stack)

