from collections import defaultdict
class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        def dfs(node):
            for neighbor in graph[node]:
                if neighbor not in marked:
                    marked.add(neighbor)
                    dfs(neighbor)

        graph = defaultdict(list)
        for account in accounts:
            name, *emails = account
            n = len(emails)
            if n > 1:
                for i in range(n):
                    graph[emails[i]].append(emails[(i+1)%n])

        marked, visited = set(), set()
        output = []
        for account in accounts:
            name, *emails = account
            marked = set()
            if emails[0] not in visited:
                marked.add(emails[0])
                dfs(emails[0])
                output.append([name] + sorted(marked))
                visited.update(marked)
        
        return output