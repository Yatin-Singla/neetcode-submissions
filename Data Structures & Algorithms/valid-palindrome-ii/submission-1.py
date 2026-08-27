class Solution:
    def validPalindrome(self, s: str) -> bool:
        left, right = 0, len(s)-1
        while left < right:
            if s[left] != s[right]:
                candidate1, candidate2 = s[left:right], s[left+1:right+1]
                return candidate1 == candidate1[::-1] or \
                candidate2 == candidate2[::-1]
            left += 1
            right -= 1

        return True
            
            