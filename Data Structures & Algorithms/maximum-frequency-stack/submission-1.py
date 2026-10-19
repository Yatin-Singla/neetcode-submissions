class FreqStack:
    def __init__(self):
        self.hashTable = defaultdict(list)
        self.counter = defaultdict(int)
        self.maxFreq = 0

    def push(self, x: int) -> None:
        self.counter[x] += 1
        self.hashTable[self.counter[x]].append(x)
        self.maxFreq = max(self.maxFreq, self.counter[x])

    def pop(self) -> int:
        x = self.hashTable[self.maxFreq].pop()
        self.counter[x] -= 1
        if not self.hashTable[self.maxFreq]:
            self.maxFreq -= 1
        return x