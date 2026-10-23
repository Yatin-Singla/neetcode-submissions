from math import inf
from collections import defaultdict, Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        window, counterT = defaultdict(int), Counter(t)
        need, have = len(counterT), 0
        minLength, start = len(s)+1, 0
        res = [-1,-1]
        for end, char in enumerate(s):
            window[char] += 1

            if char in counterT and counterT[char] == window[char]:
                have += 1

            while have == need:
                if end - start + 1 < minLength:
                    res = [start, end]
                    minLength = end - start + 1

                window[s[start]] -= 1
                if s[start] in counterT and window[s[start]] < counterT[s[start]]:
                    have -= 1
                start += 1    
        
        start, end = res
        return s[start: end + 1] if minLength != len(s)+1 else ""

        
        



