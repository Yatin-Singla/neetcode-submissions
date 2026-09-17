class Solution:
    def reorganizeString(self, s: str) -> str:
        counter = Counter(s)
        prev, n = None, len(s)
        pq = [[-freq, key] for key, freq in counter.items()]
        heapq.heapify(pq)
        output = []

        while pq or prev:
            if prev and not pq:
                return ""

            freq, key = heapq.heappop(pq)
            output.append(key)
            freq += 1

            if prev:
                heapq.heappush(pq, prev)
                prev = None
            
            if freq != 0:
                prev = [freq, key]
            
        return "".join(output)