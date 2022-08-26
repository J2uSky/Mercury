class DList:
    class Node:
        def __init__(self, prev, item, next):
            self.item = item
            self.prev = prev
            self.next = next

    def __init__(self):
        self.head = self.Node(None, None, None)
        self.tail = self.Node(self.head, None, None)
        self.head.next = self.tail
        self.size = 0

    def size(self): return self.size

    def is_empty(self): return self.size == 0

    def add(self, pos, item):
        p = self.head
        for i in range(pos):
            p = p.next
        t = p.prev
        n = self.Node(t, item, p)
        t.next = n
        p.prev = n
        self.size += 1

    def delete(self, pos):
        if self.size < pos:
            return
        p = self.head
        for i in range(pos):
            p = p.next
        t = p.prev
        q = p.next
        t.next = q
        q.prev = t
        self.size -= 1

    def get(self, pos):
        if self.size < pos:
            return "Invalid position"
        p = self.head
        for i in range(pos):
            p = p.next
        return p.item

    def print(self):
        if self.is_empty():
            print("List is empty.")
        else:
            p = self.head.next
            while p != self.tail:
                if p.next != self.tail:
                    print(p.item, end="")
                else:
                    print(p.item)
                p = p.next

if __name__ == "__main__":
    num = int(input("Number of operations : "))
    List = DList()
    for i in range(num):
        inputs = input("Input : ")
        operation = inputs[0]
        if operation == "A":
            pos = int(inputs[2:-1])
            alphabet = inputs[-1]
            List.add(pos, alphabet)
        elif operation == "D":
            pos = int(inputs[2:])
            List.delete(pos)
        elif operation == "G":
            pos = int(inputs[2:])
            print(List.get(pos))
        elif operation == "P":
            List.print()
