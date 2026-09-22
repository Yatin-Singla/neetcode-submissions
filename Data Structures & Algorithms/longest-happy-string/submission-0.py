class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        heap = []
        output = []
        for freq, char in [(-a, "a"), (-b, "b"), (-c, "c")]:
            if freq != 0:
                heapq.heappush(heap, (freq, char))
        while heap:
            freq, char = heapq.heappop(heap)
            if len(output) > 1 and output[-1] == output[-2] == char:
                if not heap:
                    break
                freq2, char2 = heapq.heappop(heap)
                output.append(char2)
                freq2 += 1
                if freq2:
                    heapq.heappush(heap, (freq2, char2))
                heapq.heappush(heap, (freq, char))
            else:
                output.append(char)
                freq += 1
                if freq:
                    heapq.heappush(heap, (freq, char))
        
        return "".join(output)
        