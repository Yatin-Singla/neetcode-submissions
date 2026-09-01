class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        indegree = {i:0 for i in range(1, n+1)}
        graph = {i:[] for i in range(1, n+1)}
        for trustee, person in trust:
            indegree[person] += 1
            graph[trustee].append(person)
        
        for i in range(1, n+1):
            if not graph[i] and indegree[i] == n-1:
                return i

        return -1