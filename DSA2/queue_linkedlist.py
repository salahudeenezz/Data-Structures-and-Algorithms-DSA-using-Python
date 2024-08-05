class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class QueueSinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def enqueue(self, data):
        nb = Node(data)
        if self.head is None:
            self.head = nb
            self.tail = nb
        else:
            nb.next = self.head
            self.head = nb
    
    def dequeue(self):
        prev = self.head
        start = self.head.next
        while start.next is not None:
            prev = prev.next
            start = start.next
        self.tail = prev
        prev.next = None
        
    
    def display(self):
        start = self.head
        while start is not None:
            print(start.data, "->", end=' ')
            start = start.next

    def peek(self):
        peek = self.tail.data
        return peek
    
    def linear_search(self, element):
        if self.head is not None:
            start = self.head
            while start is not None:
                if start.data == element:
                    return f"{element} is found in the Queue."
                else:
                    start = start.next
            return f"{element} was not found in the Queue."
            
        else:
            return None


link = QueueSinglyLinkedList()
link.enqueue(10)
link.enqueue(8)
link.enqueue(6)
link.enqueue(4)
link.enqueue(2)

link.dequeue()
link.dequeue()
link.dequeue()


link.display()
print("\n")
print(link.peek())

store = link.linear_search(4)
print(store)