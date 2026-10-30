class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        cantCommunicate = 0
        adjList = defaultdict(list)
        visited = set()

        def traverse(x,y):
            queue = deque([(x,y)])
            while queue:
                x,y = queue.popleft()
                for i, j in adjList[(x,y)]:
                    if (i,j) not in visited:
                        visited.add((i,j))
                        queue.append((i,j))

        # build adjacency list row by row
        for i in range(m):
            prev = None
            for j in range(n):
                if grid[i][j] == 1 and prev:
                    adjList[prev].append((i,j))
                    adjList[(i,j)].append(prev)
                    prev = (i,j)
                elif grid[i][j] == 1 and not prev:
                    prev = (i,j)
        
        # build adjacency list col by col
        for j in range(n):
            prev = None
            for i in range(m):
                if grid[i][j] == 1 and prev:
                    adjList[prev].append((i,j))
                    adjList[(i,j)].append(prev)
                    prev = (i,j)
                elif grid[i][j] == 1 and not prev:
                    prev = (i,j)


        for i in range(m):
            for j in range(n):
                visitedCount = len(visited)
                visited.add((i,j))
                if grid[i][j] == 1:
                    traverse(i, j)
                if len(visited) - visitedCount == 1:
                    cantCommunicate +=1

        return len(visited) - cantCommunicate            

        