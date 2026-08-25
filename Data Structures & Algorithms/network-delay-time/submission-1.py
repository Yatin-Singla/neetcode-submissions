class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for src, dest, weight in times:
            graph[src].append((weight, dest))

        visited = {}
        pq = [(0, k)]

        while pq:
            t, node = heapq.heappop(pq)
            if node not in visited:  
                visited[node] = t
                if len(visited) == n:
                    return t
                for weight, neighbor in graph[node]:
                    if neighbor not in visited:
                        heapq.heappush(pq, (t + weight, neighbor))
                    
        return -1