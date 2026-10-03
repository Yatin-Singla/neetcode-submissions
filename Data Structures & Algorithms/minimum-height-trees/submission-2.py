class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]

        graph = defaultdict(list)
        indegree = defaultdict(int)

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
            indegree[u] += 1
            indegree[v] += 1

        queue = deque()
        for node in range(n):
            if indegree[node] == 1:
                queue.append(node)
                indegree.pop(node)

        while queue:
            if n <= 2:
                return list(queue)
            for _ in range(len(queue)):
                node = queue.popleft()
                n -= 1
                for neighbor in graph[node]:
                    indegree[neighbor] -= 1
                    if indegree[neighbor] == 1:
                        indegree.pop(neighbor)
                        queue.append(neighbor)