from functools import lru_cache
class Solution:
    def numDecodings(self, s: str) -> int:
        # fi = 1 + fi+1 + cond(1) + fi+2
      
        def inBounds(num):
            return 0 < num < 27
        
        @lru_cache
        def decode(i):
            if i >= len(s):
                return 1
            if s[i] == "0":
                return 0

            nWays = 0
            if i + 1 < len(s) and inBounds(int(s[i] + s[i+1])):
                nWays += decode(i+2)
            
            nWays += decode(i+1)

            return nWays
            
        
        return decode(0)