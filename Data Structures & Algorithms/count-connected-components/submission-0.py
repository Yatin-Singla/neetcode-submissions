class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adjList = {i: [] for i in range(n)}
        for vertexA, vertexB in edges:
            adjList[vertexA].append(vertexB)
            adjList[vertexB].append(vertexA)

        def dfs(node):
            if node in visited:
                return
            
            visited.add(node)
            for neighbor in adjList[node]:
                dfs(neighbor)
            return
    
        count = 0
        visited = set()
        for i in range(n):
            if i not in visited:
                dfs(i)
                count += 1
        return count