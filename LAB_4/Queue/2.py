class MyStack:
    def __init__(self):
        self.queue1 = []
        self.queue2 = []
    def push(self, x: int):
        self.queue1.append(x)
    def pop(self) -> int:
        while len(self.queue1) > 1:
            self.queue2.append(self.queue1.pop(0))
        popped = self.queue1.pop()
        self.queue1, self.queue2 = self.queue2, self.queue1
        return popped
    def top(self) -> int:
        return self.queue1[-1]
    def empty(self) -> bool:
        return not self.queue1

myStack = MyStack()
myStack.push(1)
myStack.push(2)
print(myStack.top())
print(myStack.pop())
print(myStack.empty())
