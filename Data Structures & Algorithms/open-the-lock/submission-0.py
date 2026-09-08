class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        visited = set(deadends)
        
        if "0000" in visited:
            return -1
        
        queue = deque(["0000"])
        visited.add("0000")
        moves = 0

        while queue:
            lvlSize = len(queue)
            for _ in range(lvlSize):
                lock = queue.popleft()
                if lock == target:
                    return moves
                for i in range(4):
                    for j in (1,-1):
                        digit = str((int(lock[i]) + j + 10) % 10)
                        nextLock = lock[:i] + digit + lock[i+1:]
                        if nextLock not in visited:
                            visited.add(nextLock)
                            queue.append(nextLock)
            moves += 1

        return -1