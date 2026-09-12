from collections import OrderedDict

class LRUCache:
    def __init__(self, capacity: int):
        self.cache = OrderedDict()
        self.capacity = capacity

    def get(self, key: int) -> int:
        val = self.cache.get(key, None)
        if val is not None:
            self.cache.move_to_end(key)
        else:
            return -1

        return val

    def put(self, key: int, value: int) -> None:
        val = self.cache.get(key, None)
        # max cap
        if val is None and self.capacity == len(self.cache):
            # last=False => FIFO
            self.cache.popitem(last=False)

        # insert/update
        self.cache[key] = value
        self.cache.move_to_end(key)



            
        
