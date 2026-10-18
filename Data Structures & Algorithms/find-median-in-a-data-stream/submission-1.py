class MedianFinder:
        # idea is to keep both heaps balanced (diff in len is no more than 1 element)
        # identify where new element belongs (1st half or 2nd half)
        # default is to keep min heap (2nd half) bigger
    def __init__(self):
        # 2nd half elements
        self.min_heap = []
        # 1st half elements
        self.max_heap = []

    def addNum(self, num: int) -> None:
        if not self.min_heap and not self.max_heap:
            heapq.heappush(self.min_heap, num)
            return 

        # num belongs in first half
        if self.max_heap and num < self.max_heap[0]:
            if len(self.max_heap) == len(self.min_heap):
                heapq.heappush(self.min_heap, heapq.heappop_max(self.max_heap))
                heapq.heappush_max(self.max_heap, num)
            else:
                heapq.heappush_max(self.max_heap, num)

            return
        
        # num belongs in 2nd half
        if self.min_heap[0] < num:
            if len(self.min_heap) == len(self.max_heap):
                heapq.heappush(self.min_heap, num)
            else:
                heapq.heappush_max(self.max_heap, heapq.heappop(self.min_heap))
                heapq.heappush(self.min_heap, num)

            return


        # num is in the middle
        #if num < self.min_heap[0]: # num > self.max_heap
        if len(self.min_heap) > len(self.max_heap):
            heapq.heappush_max(self.max_heap, num)
        else: # len(self.min_heap) == len(self.max_heap) 
            heapq.heappush(self.min_heap, num)
       
        return


    def findMedian(self) -> float:
        # mean if len is equal
        if len(self.min_heap) == len(self.max_heap):
            return (self.min_heap[0] + self.max_heap[0]) / 2

        # odd len, default case min_heap len is >>. whichever has greater len has median
        return self.min_heap[0] # if len(self.min_heap) > len(self.max_heap) else self.max_heap[0]
        