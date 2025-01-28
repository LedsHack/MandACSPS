class MyCircularDeque:
    def __init__(self, k: int):
        self.capacity = k
        self.queue = [None] * k
        self.front = 0
        self.rear = 0
        self.size = 0
    def insertFront(self, value: int) -> bool:
        if self.size == self.capacity:
            return False
        self.front = (self.front - 1) % self.capacity
        self.queue[self.front] = value
        self.size += 1
        return True
    def insertLast(self, value: int) -> bool:
        if self.size == self.capacity:
            return False
        self.queue[self.rear] = value
        self.rear = (self.rear + 1) % self.capacity
        self.size += 1
        return True
    def deleteFront(self) -> bool:
        if self.size == 0:
            return False
        self.front = (self.front + 1) % self.capacity
        self.size -= 1
        return True
    def deleteLast(self) -> bool:
        if self.size == 0:
            return False
        self.rear = (self.rear - 1) % self.capacity
        self.size -= 1
        return True
    def getFront(self) -> int:
        if self.size == 0:
            return -1
        return self.queue[self.front]
    def getRear(self) -> int:
        if self.size == 0:
            return -1
        return self.queue[(self.rear - 1) % self.capacity]
    def isEmpty(self) -> bool:
        return self.size == 0
    def isFull(self) -> bool:
        return self.size == self.capacity
myCircularDeque = MyCircularDeque(3)
print(myCircularDeque.insertLast(1))
print(myCircularDeque.insertLast(2))
print(myCircularDeque.insertFront(3))
print(myCircularDeque.insertFront(4))
print(myCircularDeque.getRear())
print(myCircularDeque.isFull())
print(myCircularDeque.deleteLast())
print(myCircularDeque.insertFront(4))
print(myCircularDeque.getFront())
