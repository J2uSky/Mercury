class TNode:
    def __init__ (self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

F4 = TNode('70', None, None)
F5 = TNode('90', None, None)
F2 = TNode('30', F4, F5)
F7 = TNode('130', None, None)
F8 = TNode('80', None, None)
F6 = TNode('120', F7, F8)
F3 = TNode('50', None, F6)
root = TNode('20', F2, F3)

F1 = TNode(root.data)
F1.left = F2
F1.right = F3
F2.left = F4
F2.right = F5
F3.right = F6
F6.left = F7
F6.right = F8

inputs = input()
if inputs == '1':
    print(F1.data)
elif inputs == '2':
    print(F2.data, F4.data, F5.data)
elif inputs == '3':
    print(F3.data, F6.data)
elif inputs == '4':
    print(F4.data)
elif inputs == '5':
    print(F5.data)
elif inputs == '6':
    print(F6.data, F7.data, F8.data)
elif inputs == '7':
    print(F7.data)
elif inputs == '8':
    print(F8.data)
else:
    print("-1")

