class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counter = Counter(tasks)
        clock = 0
        pq = [(-freq, key) for key, freq in counter.items()]
        cooldown = deque()
        
        heapq.heapify(pq)

        while pq or cooldown:
            clock += 1
            while cooldown and clock == cooldown[0][0]: # process most freq elements
                _, key, freq = cooldown.popleft()
                heapq.heappush(pq, (-freq, key))
            if pq:
                freq, key = heapq.heappop(pq)
                freq += 1
                if freq != 0:
                    cooldown.append((clock + n + 1, key, abs(freq)))
            else: # jump time
                clock = cooldown[0][0] - 1
            
        return clock