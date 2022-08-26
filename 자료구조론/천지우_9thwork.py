MAX_QSIZE = int(input("size of CircularQueue : "))
class CircularQueue:
    def __init__(self):
        self.front = 0
        self.rear = 0
        self.items = [0] * MAX_QSIZE
    def isEmpty(self):return self.front == self.rear
    def isFull(self):return self.front == (self.rear+1)%MAX_QSIZE
    def enqueue(self, item):
        if not self.isFull():
            self.rear = (self.rear+1)%MAX_QSIZE
            self.items[self.rear] = item
    def dequeue(self):
        if not self.isEmpty():
            self.front = (self.front+1)%MAX_QSIZE
            self.items[self.front] = 0
            return self.items[self.front]

    def peek(self):
        if not self.isEmpty():
            return self.items[(self.front + 1) % MAX_QSIZE]

    def size(self):
        return (self.rear - self.front + MAX_QSIZE) % MAX_QSIZE

    def display(self):
        out = []
        if self.front < self.rear:
            out = self.items
        else:
            out = self.items[0:self.rear + 1] + self.items[self.front:MAX_QSIZE]
        print(out)

q = CircularQueue()
n = int(input("Number of operations : "))
for i in range(n):
    inputs = input()
    operation = inputs[0]
    if q.isFull():
        if operation == "I":
            print("overflow", q.display())
            break
    elif operation == "I":
        num = int(inputs[2:])
        q.enqueue(num)
    elif operation == "D":
        q.dequeue()
        if q.isEmpty():
            print("underflow")
            break
    elif operation == "P":
        q.display()