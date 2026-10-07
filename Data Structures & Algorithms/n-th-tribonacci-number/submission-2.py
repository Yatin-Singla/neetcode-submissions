class Solution:
    def tribonacci(self, n: int) -> int:
        if n <= 0:
            return 0
        elif n == 1 or n == 2:
            return 1
            
        n0, n1, n2 = 0, 1, 1
        for i in range(3,n+1):
            ni = n2 + n1 + n0
            n2, n1, n0 = ni, n2, n1

        return n2