

class stack:

    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        self.stack.pop()

    def traverse(self):

        for i in self.stack:
            print(i, end=" ")
        print()

    def tos(self):
        print(self.stack(len(self.stack) - 1))


s = stack()

s.push(10)
s.push(20)
s.push(30)
s.push(40)
s.push(50)

s.traverse()

s.pop()
s.pop()
s.pop()

s.traverse()
