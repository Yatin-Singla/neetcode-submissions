from math import inf
class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        tasksCompleted = []
        heap, backlog = [], []
        clock = inf

        for i, (enqueue, process) in enumerate(tasks):
            heapq.heappush(heap, (enqueue, process, i))
            clock = min(clock, enqueue)

        while heap or backlog:
            while heap and heap[0][0] <= clock:
                _, process, i = heapq.heappop(heap)
                heapq.heappush(backlog, (process, i))

            if backlog:
                processTime, idx = heapq.heappop(backlog)
                clock += processTime
                tasksCompleted.append(idx)

            if not backlog and heap and clock < heap[0][0]:
                clock = heap[0][0]

        return tasksCompleted