class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        def dfs(node, target):
            if node == target:
                return 1

            for neighbor, val in graph[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    result = dfs(neighbor, target)
                    if result >= 0:
                        return result*val

            return -1

        graph = defaultdict(list)
        output = []
        for i, [num, den] in enumerate(equations):
            graph[num].append([den, values[i]])
            if values[i] != 0:
                graph[den].append([num, 1/values[i]])


        for start, target in queries:
            visited = set([start])
            if start not in graph or target not in graph:
                output.append(-1)
                continue
            output.append(dfs(start, target))

        return output 