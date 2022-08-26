class Stack :
    def __init__(self):
        self.top = []

    def isEmpty(self): return len(self.top) == 0
    def size(self): return len(self.top)
    def clear(self): self.top = []

    def push(self, item):
        self.top.append(item)

    def pop(self):
        if not self.isEmpty():
            return self.top.pop(-1)

    def peek(self):
        if not self.isEmpty():
            return self.top[-1]

def checkBrackets(statement):
    n=0
    stack = Stack()
    for ch in statement:
        if ch in ('{', '[', '('):
            stack.push(ch)

        elif ch in ('}', ']', ')'):
            if stack.isEmpty():
                return False
            else:
                left = stack.pop()
                if (ch == "}" and left != "{") or \
                    (ch == "]" and left != "[") or \
                    (ch == ")" and left != "("):
                    return False

    return stack.isEmpty()

str = str(input("입력 :"))
n=0
for s in str:
    if (s=="(" or s == "{" or s == "[" or s == ")" or s== "}" or s == "]"):
        n+=1
m = checkBrackets(str)
if checkBrackets(str) == False:
    m = 'Wrong'
else:
    m = 'OK'

print(m,'_',n)