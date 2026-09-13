from collections import OrderedDict
class LFUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.minFreq = 0
        # store key: [val, freq]
        self.counter = {}
        # store freq: orderedDict(keys) [ordered dict is important to access a particular key in O(1)]
        # problem can be solved by using DLL/deque instead of orderedDict
        # however updating freq for key upon get becomes O(n) instead of O(1)
        self.freqMap = defaultdict(OrderedDict)

    def get(self, key: int) -> int:
        if key in self.counter:
            val, freq = self.counter[key]
            self.counter[key][1] += 1
            
            del self.freqMap[freq][key]
            if freq == self.minFreq and len(self.freqMap[freq]) == 0:
                self.minFreq += 1

            self.freqMap[freq+1][key] = None
            return val

        return -1
        

    def put(self, key: int, value: int) -> None:
        val = self.get(key)
        # make room
        if val == -1 and len(self.counter) == self.capacity:
            # del FIFO
            popKey, _ = self.freqMap[self.minFreq].popitem(last = False)
            del self.counter[popKey]

        # new insert but capacity not max
        if val == -1:
            self.counter[key] = [value, 1]
            self.minFreq = 1
            self.freqMap[1][key] = None
        else:
            self.counter[key][0] = value