class Node:
    def __init__(self, val, next = None, prev = None):
        self.val = val
        self.next = next
        self.prev = prev

class MyCircularQueue:

    def __init__(self, k: int):
        self.capacity = k   
        self.size = 0
        self.head = Node(-1)
        self.tail = Node(-1)

        self.head.next = self.head.prev = self.tail
        self.tail.next = self.tail.prev = self.head


    def enQueue(self, value: int) -> bool:
        # what if size == capacity?
        if self.isFull():
            return False

        tail = self.tail.prev
        node = Node(value)
        tail.next = node
        node.prev = tail
        self.tail.prev = node
        node.next = self.tail
        self.size += 1
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False

        head = self.head.next
        self.head.next = head.next
        head.next.prev = self.head
        self.size -= 1
        return True

    def Front(self) -> int:
        if self.isEmpty():
            return -1

        return self.head.next.val

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        
        return self.tail.prev.val

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == self.capacity


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()