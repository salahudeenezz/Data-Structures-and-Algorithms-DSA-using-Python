class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
    
    def enqueue(self, data):
        element_1 = Node(data)
        self.front = element_1
    
    def enqueue2(self, data):
        element_2 = Node(data)
        element_2.next = self.front
        self.rear = element_2
    
    def enqueue3(self, data):
        element_3 = Node(data)
        element_3.next = self.rear
        self.rear = element_3
    
    def dequeue(self):
        prev = self.rear
        start = self.rear.next
        while start.next:
            start = start.next
            prev = prev.next
        prev.next = None
        self.front = prev

    
    def display(self):
        start = self.rear
        while start:
            print(start.data, '->', end=' ')
            start = start.next


link = Queue()

link.enqueue(10)
link.enqueue2(20)
link.enqueue3(30)

link.dequeue()
link.dequeue()

link.display()
