from collections import deque

class Solution:
    def numSquares(self, n: int) -> int:
        squares = [i * i for i in range(1, int(n**0.5) + 1)]
        queue = deque([n])
        visited = set([n])
        level = 0
        
        while queue:
            level += 1
            for _ in range(len(queue)):
                curr = queue.popleft()
                for sq in squares:
                    rem = curr - sq
                    if rem == 0:
                        return level
                    if rem > 0 and rem not in visited:
                        visited.add(rem)
                        queue.append(rem)
        return level