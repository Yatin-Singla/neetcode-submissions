class Solution:
    def validPalindrome(self, s: str) -> bool:
        def isPalindrome(low, high):
            while low < high:
                if s[low] != s[high]:
                    return False
                low += 1
                high -= 1
            return True

        low, high = 0, len(s)-1
        while low < high:
            if s[low] != s[high]:
                return isPalindrome(low, high-1) or isPalindrome(low+1,high)
            low += 1
            high -= 1
        
        return True
            
            