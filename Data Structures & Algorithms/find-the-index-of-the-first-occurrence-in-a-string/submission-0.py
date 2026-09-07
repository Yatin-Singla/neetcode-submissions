from functools import reduce
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n, m = len(needle), len(haystack)
        if m < n:
            return -1
        
        start, base = 0, 26
        higherOrder = base ** (n-1)
        hashSum = reduce(lambda acc, pair: acc + (ord(pair[1]) * (base**(n-1-pair[0]))), enumerate(needle), 0)
        currSum = reduce(lambda acc, pair: acc + (ord(pair[1])*(base ** (n-1-pair[0]))), enumerate(haystack[:n]), 0)

        for end in range(n,m):
            if currSum == hashSum:
                return start
            
            currSum = (currSum - ord(haystack[start])*higherOrder)*base + ord(haystack[end])
            start += 1

        if currSum == hashSum:
            return start

        return -1