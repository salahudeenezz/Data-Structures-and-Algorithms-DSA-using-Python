class Queue:
    def __init__(self):
        self.queue = list()
    
    def push(self, element):
        self.queue.append(element)
    
    def pop(self):
        self.queue.pop(0)
    
    def peek(self):
        if self.queue:
            return self.queue[-1]
        else:
            return False
    
    def display(self):
        print(self.queue)


queue = Queue()

queue.push(1)
queue.push(2)
queue.push(3)
queue.push(4)
queue.push(5)

queue.pop()
queue.pop()
queue.pop()

store = queue.peek()

queue.display()

print(f'\nThe element {store} is peeked.')