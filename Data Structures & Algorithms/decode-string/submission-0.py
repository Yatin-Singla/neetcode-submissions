class Solution:
    def decodeString(self, s: str) -> str:
        numStack, stack = [], []
        i = 0

        while i < len(s):
            if s[i].isdigit():
                num = 0
                while s[i].isdigit():
                    num = num*10 + int(s[i])
                    i += 1
                numStack.append(num)
                i -= 1
            elif s[i] == "[":
                stack.append([])
            elif s[i].isalpha():
                # assuming len(stack) at min is 1
                if stack:
                    stack[-1].append(s[i])
                else:
                    stack.append([s[i]])
            else:
                digit, ch = numStack.pop(), ''.join(stack.pop())
                if stack:
                    stack[-1].append(ch*digit)
                else:
                    stack.append([ch*digit])

            i += 1

        return ''.join(stack[-1])