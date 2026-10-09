class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 1 or x == 0:
            return x
        low, high = 0, x >> 1
        ans = 0
        while low <= high:
            mid = (low + high) >> 1
            if x - (mid*mid) == 0:
                return mid
            elif x - (mid*mid) < 0:
                high = mid - 1
            elif x - (mid*mid) < x - (ans*ans):
                ans = mid
                low = mid + 1
            else:
                low = mid + 1

        return ans
