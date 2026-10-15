from functools import lru_cache
class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expand(left, right):
            nonlocal res_len, res_start
            while left > -1 and right < n and s[left] == s[right]:
                if right - left + 1 > res_len:
                    res_len = right - left + 1
                    res_start = left

                left -= 1
                right += 1

        # f(i) = cond(i + f(i-1)), i  
        # f(i) = longest palindromic substring from [i,j]; i <= j < n
        n = len(s)
        res_len = res_start = 0

        for center in range(n):
            left = right = center
            # odd length
            expand(left, right)

            # even length
            left, right = center, center + 1
            expand(left, right)

        return s[res_start:res_start+res_len]
            
