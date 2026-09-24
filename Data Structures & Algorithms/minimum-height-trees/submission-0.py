class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        MHT = []
        minHeight = height = n
        
        def dfs(node):
            height = 0
            for neighbor in graph[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    height = max(height, dfs(neighbor))

            return height + 1

        graph = defaultdict(list)
        for v1, v2 in edges:
            graph[v1].append(v2)
            graph[v2].append(v1)

        for i in range(n):
            visited = set([i])
            height = dfs(i)
            if height < minHeight:
                minHeight = height
                MHT = [i]
            elif height == minHeight:
                MHT.append(i)

        return MHT