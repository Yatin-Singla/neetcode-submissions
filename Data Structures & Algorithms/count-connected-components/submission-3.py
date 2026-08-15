class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        visited, graph = set(), defaultdict(list)
        count = 0

        for v1, v2 in edges:
            graph[v1].append(v2)
            graph[v2].append(v1)

        def dfs(node):
            visited.add(node)
            for neighbor in graph[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    dfs(neighbor)

            return 1

        for i in range(n):
            if i not in visited:
                count += dfs(i)

        return count