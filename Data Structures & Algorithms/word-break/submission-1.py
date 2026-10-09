from functools import lru_cache
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # recurrence relation
        # options (and pick valid)
        # no break, f(i+1:n) + break @i (from begining) 
        wordDict = set(wordDict)
        @lru_cache()
        def recurse(start):
            if start == len(s):
                return True

            for end in range(start+1, len(s)+1):
                if s[start:end] in wordDict and recurse(end):
                    return True

            return False

        return recurse(0)
            