class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        graph = defaultdict(set)
        for src, dest in edges:
            graph[src].add(dest)
            graph[dest].add(src)
        
        visited = set()

        def dfs(root):
            if root in visited:
                return False
            
            visited.add(root)
            neighbors = list(graph[root])
            for neighbor in neighbors:
                graph[root].discard(neighbor)
                graph[neighbor].discard(root)
                if neighbor in visited:
                    return False
                if not dfs(neighbor):
                    return False
            return True

        return dfs(0) and len(visited) == n