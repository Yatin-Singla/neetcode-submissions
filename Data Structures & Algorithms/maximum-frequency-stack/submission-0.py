class Node:
    def __init__(self, key, next = None):
        self.key = key
        self.next = next

class Stack:
    def __init__(self):
        self.head = Node(-1)
        self.length = 0

    def push(self, key):
        newNode = Node(key, self.head.next)
        self.head.next = newNode
        self.length += 1 

    def pop(self, key = None):
        # if key:
        #     prev, curr = self.head, self.head.next
        #     while curr and curr.key != key:
        #         prev = curr
        #         curr = curr.next

        #     prev.next = curr.next
        #     # assuming key exists
        #     self.length -= 1
        #     return curr.key
        if self.head.next:
            popNode = self.head.next
            self.head.next = popNode.next
            self.length -= 1
            return popNode.key
        
        return -1

class FreqStack:
    # opp of LFU cache?
    def __init__(self):
        # maintain freqMap stores key and freq
        self.freqMap = defaultdict(int)
        # bucket map stores freq with LL as value
        self.bucketMap = defaultdict(Stack)
        # maxFreq variable
        self.maxFreq = 0

    def push(self, key: int) -> None:
        # update bucket
        # remove node from LL of prev Freq
        # if key in self.freqMap:
        #     self.bucketMap[self.freqMap[key]].pop(key)

        # update freqMap
            # increment freq
        self.freqMap[key] += 1
        # append node to tail of new freq
        self.bucketMap[self.freqMap[key]].push(key)

        # update maxFreq if needed
        self.maxFreq = max(self.maxFreq, self.freqMap[key])
            

    def pop(self) -> int:
        # pop tail (automatically closer to top of stack)
        key = self.bucketMap[self.maxFreq].pop()
        self.freqMap[key] -= 1
        
        # update maxFreq if bucket is now empty
        if self.bucketMap[self.maxFreq].length == 0:
            self.maxFreq -= 1

        return key


