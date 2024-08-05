class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_beginning(self, data):
        nb = Node(data)
        nb.next = self.head
        self.head = nb
        self.tail.next = self.head

    def insert_end(self, data):
        ne = Node(data)
        start = self.head
        while start.next != self.head:
            start = start.next
        start.next = ne
        self.tail = ne
        self.tail.next = self.head

    def insert_position(self, data, pos):
        np = Node(data)
        start = self.head
        for i in range(pos-1):
            start = start.next
        np.next = start.next
        start.next = np
        
    def display(self):
        start = self.head
        print(start.data, '->', end=' ')
        while start.next != self.head:
            start = start.next
            print(start.data, '->', end=' ')
        print(start.next.data)


n1 = Node(1)
link = CircularLinkedList()
link.head = n1
link.tail = n1
link.tail.next = link.head

n2 = Node(2)
link.tail.next = n2
link.tail = n2
link.tail.next = link.head

link.insert_beginning(0)
link.insert_end(3)
link.insert_position(5, 2)

link.display()
