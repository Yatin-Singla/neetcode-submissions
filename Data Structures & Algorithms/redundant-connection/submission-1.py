class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        visited, redConn = set([1]), set()
        graph = defaultdict(list)
        startNode = None

        for a,b in edges:
            graph[a].append(b)
            graph[b].append(a)

        def dfs(node, parent):
            nonlocal startNode
            for neighbor in graph[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    if dfs(neighbor, node):
                        redConn.add((node, neighbor))
                        redConn.add((neighbor, node))
                        return node != startNode
                elif neighbor in visited and neighbor != parent:
                    startNode = neighbor
                    redConn.add((node, neighbor))
                    redConn.add((neighbor, node))
                    return True

        dfs(1, 0)
        
        for i in range(len(edges)-1, -1, -1):
            a,b = edges[i]
            if (a,b) in redConn:
                return edges[i]
                