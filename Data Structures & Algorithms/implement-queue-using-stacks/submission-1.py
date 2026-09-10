class MyQueue:

    def __init__(self):
        self.insertStack = []
        self.popStack = []

    def push(self, x: int) -> None:
        while self.popStack:
            # insert all elements to insert stack. and push 
            self.insertStack.append(self.popStack.pop())

        self.insertStack.append(x)

    def pop(self) -> int:
        while self.insertStack:
            # flip all elements to popstack and pop
            self.popStack.append(self.insertStack.pop())

        if self.popStack:
            return self.popStack.pop()


    def peek(self) -> int:
        while self.insertStack:
            self.popStack.append(self.insertStack.pop())

        if self.popStack:
            return self.popStack[-1]
        

    def empty(self) -> bool:
        return bool(len(self.insertStack)==0 and len(self.popStack)==0)


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()