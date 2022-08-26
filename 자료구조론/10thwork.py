MAX_QSIZE = 10


class CircularDeque:

    def __init__(self):
        self.front = 0
        self.rear = 0
        self.items = [None] * MAX_QSIZE

    def isEmpty(self):
        return self.front == self.rear

    def isFull(self):
        return self.front == (self.rear + 1) % MAX_QSIZE

    def size(self):
        return (self.rear - self.front + MAX_QSIZE) % MAX_QSIZE

    def addRear(self, item):
        if not self.isFull():
            self.rear = (self.rear + 1) % MAX_QSIZE
            self.items[self.rear] = item

    def deleteFront(self):
        if not self.isEmpty():
            self.front = (self.front + 1) % MAX_QSIZE
            return self.items[self.front]

    def getFront(self):
        if not self.isEmpty():
            return self.items[(self.front + 1) % MAX_QSIZE]

    def addFront(self, item):
        if not self.isFull():
            self.items[self.front] = item
            self.front = self.front - 1
            if self.front < 0: self.front = MAX_QSIZE - 1

    def deleteRear(self):
        if not self.isEmpty():
            item = self.items[self.rear];
            self.rear = self.rear - 1
            if self.rear < 0: self.rear = MAX_QSIZE - 1
            return item

    def getRear(self):
        return self.items[self.rear]

    def display(self):
        out = []
        if self.front < self.rear:
            out = self.items[self.front + 1:self.rear + 1]
        else:
            out = self.items[self.front + 1:MAX_QSIZE] \
                  + self.items[0:self.rear + 1]
        for i in range(len(out)):
            print(out[i], end = ' ')

dq = CircularDeque()
n = int(input("number of operation : "))
for i in range(n):
    inputs = input()
    operation = inputs[:2]
    if operation == 'AF':
        num = int(inputs[3:])
        dq.addFront(num)
    elif operation == 'AR':
        num = int(inputs[3:])
        dq.addRear(num)
    elif operation == 'DF':
        dq.deleteFront()
        if dq.isEmpty():
            print("underflow")
            break
    elif operation == 'DR':
        dq.deleteRear()
        if dq.isEmpty():
            print("underflow")
            break
    elif operation == 'P':
        print(' ', end='')
        dq.display()
        print()