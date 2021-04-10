
class queue:

    def __init__(self):
        self.queue = []


    def enqueue(self, item):
        self.queue.append(item)
    
    def dequeue(self):
        self.queue.pop(0)

    def traverse(self):
        for i in self.queue:
            print(i, end = " ")
        print()


q = queue()

q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.enqueue(40)
q.enqueue(50)

q.traverse()

q.dequeue()
q.dequeue()
q.dequeue()

q.traverse()