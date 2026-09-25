class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        
        def bfs(start, target):
            visited = set([start])
            queue = deque([(start, 1)])

            while queue:
                node, total = queue.popleft()
                if node == target:
                    output.append(total)
                    return
                for neighbor, val in graph[node]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append((neighbor, total*val))

            output.append(-1)
            return

        graph = defaultdict(list)
        output = []
        for i, [num, den] in enumerate(equations):
            graph[num].append([den, values[i]])
            if values[i] != 0:
                graph[den].append([num, 1/values[i]])


        for start, target in queries:
            if start not in graph or target not in graph:
                output.append(-1)
                continue
            bfs(start, target)
            
        return output 