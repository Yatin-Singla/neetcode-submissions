class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        count = 0

        def expand(left, right):
            nonlocal count
            while left > -1 and right < n and s[left] == s[right]:
                count += 1
                left -= 1
                right += 1

        for i in range(n):
            # even length palindrome
            left, right = i, i+1
            expand(left, right)

            left = right = i
            expand(left, right)

        return count