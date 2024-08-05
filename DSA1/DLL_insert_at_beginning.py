class Node:
    def __init__(self, data : int):
        self.data = data
        self.next = None
        self.prev = None


class DLL:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def insert_at_beginning(self, data : int):
        node_beginning = Node(data)
        node_beginning.next = self.head
        self.head.prev = node_beginning
        self.head = node_beginning
    
    def display(self):
        start = self.head
        while start is not None:
            print(start.data, '->', end=' ')
            start = start.next
    
    def display1(self):
        start = self.tail
        print('\n')
        while start is not None:
            print(start.data, '->', end=' ')
            start = start.prev

n1 = Node(10)
link = DLL()
link.head = n1
n2 = Node(20)
n1.next = n2
n2.prev = n1
link.tail = n2

link.insert_at_beginning(5)

link.display()
link.display1()