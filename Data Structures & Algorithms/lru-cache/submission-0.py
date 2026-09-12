class ListNode:
    def __init__(self, key, val, next = None, prev = None):
        self.key = key
        self.val = val
        self.next = next
        self.prev = prev

class LinkedList:
    def __init__(self, head = ListNode(-1, -1), tail = ListNode(-1, -1)):
        self.head = head
        self.tail = tail

        self.head.next = self.tail
        self.tail.prev = self.head

class LRUCache:
    def __init__(self, capacity: int):
        self.linkedList = LinkedList()
        self.cache = {}
        self.capacity = capacity

    def get(self, key: int) -> int:
        node = self.cache.get(key, None)
        if node:
            # update linked list
            node.prev.next = node.next
            node.next.prev = node.prev
            tail = self.linkedList.tail
            tail.prev.next = node
            # update node
            node.prev = tail.prev
            node.next = tail
            tail.prev = node
        else:
            return -1

        return node.val

    def put(self, key: int, value: int) -> None:
        node = self.cache.get(key, None)
        # max cap
        if not node and self.capacity == len(self.cache):
            # remove LRU (# head --> dummy node)
            tmp = self.linkedList.head.next
            self.linkedList.head.next = tmp.next
            tmp.next.prev = self.linkedList.head
            
            #book keeping
            del self.cache[tmp.key]
            del tmp

        # insert/update
        if node:
            self.cache[key].val = value
            node = self.cache[key]
            node.prev.next = node.next
            node.next.prev = node.prev
        else:
            node = ListNode(key, value)
            self.cache[key] = node

        tail = self.linkedList.tail
        
        tail.prev.next = node
        node.prev = tail.prev
        node.next = tail
        tail.prev = node



            
        
