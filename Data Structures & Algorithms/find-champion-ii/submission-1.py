class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        if not edges:
            return 0 if n == 1 else -1

        outDegree = defaultdict(int)
        adjList = defaultdict(list)
        visited = set()

        for u, v in edges:
            outDegree[u] += 1
            adjList[u].append(v)

        champion, edgeCount = -1, 0
        for key, val in outDegree.items():
            if val > edgeCount:
                edgeCount = val
                champion = key

        queue = deque([champion])
        visited.add(champion)
        
        while queue:
            node = queue.popleft()
            for neighbor in adjList[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)

        return champion if len(visited) == n else -1

        