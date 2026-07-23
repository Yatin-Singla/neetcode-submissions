class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adjList = {i: set() for i in range(n)}
        for nodeA, nodeB in edges:
            adjList[nodeA].add(nodeB)
            adjList[nodeB].add(nodeA)
        
        visited = set([0])
        queue = deque([0])
        while queue:
            node = queue.popleft()
            for neighbor in adjList[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    adjList[neighbor].discard(node)
                    queue.append(neighbor)
                else:
                    return False
            
        return len(visited) == n