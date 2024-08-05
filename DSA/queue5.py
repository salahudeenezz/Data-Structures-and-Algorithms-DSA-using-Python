class Element:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.rear = None
        self.front = None
    
    def enqueue(self, data):
        new_element = Element(data)
        new_element.next = self.rear
        self.rear = new_element
    
    def dequeue(self):
        prev = self.rear
        start = self.rear.next
        while start.next:
            prev = prev.next
            start = start.next
        prev.next = None
        self.front = prev
    

    def display(self):
        start = self.rear
        while start:
            print(start.data, '->', end=' ')
            start = start.next
        
    def peek(self):
        if self.front:
            return self.front.data
        else:
            return None


element_1 = Element(10)
link = Queue()
link.front = element_1
element_2 = Element(20)
link.rear = element_2
element_2.next = element_1

link.enqueue(30)
link.enqueue(40)
link.enqueue(50)

link.dequeue()
link.dequeue()
link.dequeue()
link.dequeue()

link.display()

store = link.peek()
print(f"\n{store}")