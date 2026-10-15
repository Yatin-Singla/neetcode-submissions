from functools import lru_cache
class Solution:
    def longestPalindrome(self, s: str) -> str:
        # dp[i][j] -> substring [i:j] is a palindrome
        n = len(s)
        res_len, res_start = 1, 0
        dp = [[False]*n for _ in range(n)]

        for i in range(n):
            dp[i][i] = True

        for i in range(n-1):
            if s[i] == s[i+1]:
                dp[i][i+1] = True
                res_start = i
                res_len = 2

        for length in range(3, n+1):
            for i in range(n - length + 1):
                j = i + length - 1
                if s[i] == s[j] and dp[i+1][j-1]:
                    dp[i][j] = True
                    if length > res_len:
                        res_start = i
                        res_len = length


        return s[res_start:res_start+res_len]
            
