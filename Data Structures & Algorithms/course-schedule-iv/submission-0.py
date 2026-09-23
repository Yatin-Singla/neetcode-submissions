from functools import lru_cache
class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        @lru_cache(maxsize = None)
        def dfs(parent, target):
            if parent == target:
                return True

            for course in graph[parent]:
                if course not in visited:
                    visited.add(course)
                    if dfs(course, target):
                        return True

            return False

        output = []
        graph = {i: [] for i in range(numCourses)}
        
        for preReq, course in prerequisites:
            graph[preReq].append(course)

        for a, b in queries:
            visited = set()
            output.append(dfs(a, b))

        return output
        