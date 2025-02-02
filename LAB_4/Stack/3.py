class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []
    def push(self, val: int):
        self.stack.append(val)
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)
    def pop(self):
        if self.stack:
            popped = self.stack.pop()
            if popped == self.min_stack[-1]:
                self.min_stack.pop()
    def top(self) -> int:
        return self.stack[-1] if self.stack else None
    def getMin(self) -> int:
        return self.min_stack[-1] if self.min_stack else None


minStack = MinStack()
minStack.push(-2)
minStack.push(0)
minStack.push(-3)
print(minStack.getMin())
minStack.pop()
print(minStack.top())
print(minStack.getMin())
