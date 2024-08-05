class Element:
    def __init__(self, data):
        self.data = data
        self.next = None
        
class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue(self, data):
        element = Element(data)
        if self.head is None:
            self.head = element
        else:
            element.next = self.head
            self.head = element
            
    def dequeue(self):
        prev = self.head
        start = self.head.next
        while start.next != None:
            prev = prev.next
            start = start.next
        prev.next = None

    def peek(self):
        start = self.head
        while start.next != None:
            start = start.next
        peek = start.data
        return peek

    def display(self):
        start = self.head
        while start:
            print(start.data, '->', end=' ')
            start = start.next
    
        
    def search(self, element):
        start = self.head
        while start is not None:
            if start.data == element:
                return start
            start = start.next
        return None

queue = Queue()
queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)
queue.enqueue(40)
queue.enqueue(50)

queue.dequeue()
queue.dequeue()
queue.dequeue()
queue.dequeue()

queue.display()
print("\n")
print(queue.peek())

store_result = queue.search(50)
if store_result is not None:
    print(f"{store_result.data} is found in the stack linked list.")
else:
    print(store_result)