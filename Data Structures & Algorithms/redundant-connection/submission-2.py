class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        indegree = defaultdict(int)

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
            indegree[u] += 1
            indegree[v] += 1

        queue = deque()
        for i in range(1,len(edges)+1):
            if indegree.get(i,0) == 1:
                queue.append(i)
                del indegree[i]

        while queue:
            node = queue.popleft()
            for neighbor in graph[node]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 1:
                    queue.append(neighbor)
                    indegree.pop(neighbor)


        for i in range(len(edges)-1, -1, -1):
            u, v = edges[i]
            if indegree.get(u, 0) > 0 and indegree.get(v,0) > 0:
                return [u,v]



        
        
                