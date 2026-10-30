class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        champions, indegree = [], {i:0 for i in range(n)}
        for u, v in edges:
            indegree[v] += 1

        for node, indegreeCount in indegree.items():
            if indegreeCount == 0:
                champions.append(node)
        
        return -1 if len(champions) > 1 else champions[-1]

        