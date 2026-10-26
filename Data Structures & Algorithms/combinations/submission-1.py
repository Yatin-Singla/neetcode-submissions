class Solution:
    def combine(self, n: int, k: int) -> list[list[int]]:      
        currComb, output = [], []
        def combinations(idx):
            if len(currComb) == k:
                output.append(currComb[::])
                return 

            for i in range(idx,n+1):
                currComb.append(i)
                combinations(i+1)
                currComb.pop()
                
            return

        combinations(1)
        return output